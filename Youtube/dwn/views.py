from django.shortcuts import render, redirect
from .code import pytube_mng
from Youtube.settings import BASE_DIR
from django.views import View
import requests
import json

# """https://youtu.be/aM9-zFvH6kI?si=JQ5uOV27NeM5JwZW"""

# def download(link, file_name):
#     r = requests.get(link, stream = True)
#     with open(BASE_DIR/'media'/'output'/file_name, 'wb') as f: 
#         for chunk in r.iter_content(chunk_size = 1024*1024): 
#             if chunk: 
#                 f.write(chunk) 
#     return "/media/output/"+file_name


class Video(View):
    
    display_error = False
    display_streams = False
    
    def get(self, request):
        url :str = request.GET.get("url","")
        if url.find("list=") > -1:
            return redirect("playlist/?purl="+url)
        if url != "":
            try:
                youtube_object = pytube_mng.get_object(url)
                self.display_streams = True 
                description = youtube_object.description
                if description == None:
                    description = ""        
                return render(request, 'dwn/index.html', {
                    "title":youtube_object.title,
                    "duration":pytube_mng.get_length(youtube_object),
                    "thumbnail":youtube_object.thumbnail_url,
                    "streams":youtube_object.streams,
                    "description":description,
                    "link":"value="+url,
                    "error":self.display_error,
                    "display_streams":self.display_streams,
                    })
            except Exception as e:
                print(e)
                self.display_streams = False
                self.display_error = True
        return render(request, "dwn/index.html", {
            "error":self.display_error,
            "display_streams":self.display_streams,
            })
    
    def post(self, request):
            return render(request, "dwn/index.html", {
                "error":self.display_error,
                "display_streams":self.display_streams,
                })
        
class Playlist(View):
    
    display_error = False
    display_videos = False
    
    def get(self, request):
        url = request.GET.get("purl", "")
        if url.find("watch?v=") > -1:
            return redirect("/?url="+url)
        if url != "":
            request.session["purl"] = url
            try:
                del request.session["videos"]
            except:
                pass
            try:
                playlist_object = pytube_mng.get_playlist(url)
                videos = playlist_object.videos
                urls = list(playlist_object.video_urls)
                
                title = playlist_object.title
                length = playlist_object.length
                thumbnail = videos[0].thumbnail_url
                
                videos = pytube_mng.get_videos_data(videos)
                self.display_videos = True
                
                request.session["videos"] = videos
                request.session["purl"] = url
                request.session["urls"] = urls
            
                return render(request, 'dwn/playlist.html', {
                    "playlist":playlist_object,
                    "videos":videos,
                    "title":title,
                    "length":length,
                    "thumbnail":thumbnail,
                    "all_urls":urls,
                    "error":self.display_error,
                    "display_videos":self.display_videos,
                    "link":"value="+url,
                })
            except Exception as e:
                print(e)
                self.display_error = True
        return render(request, "dwn/playlist.html", {
            "error":self.display_error,
            "display_videos":self.display_videos,
            })
    
    def post(self, request):
        return redirect("playlist")
    
class PlaylistDownload(View):
    
    def get(self, request):
        url = request.session.get("purl", "")
        videos = request.session.get("videos", False)
        
        if videos:
            for i in range(len(videos)):
                try:
                    if videos[i].get("streams",False):
                        pass
                    else:
                        videos[i]["streams"] = pytube_mng.get_streams_data(pytube_mng.get_object(videos[i]["url"]))
                    print(f"Video {i:>3}: fetched")
                except Exception as e:
                    print(f"Video {i:>3}: not fetched due to "+e.__str__)

            request.session["videos"] = videos
            return render(request, "dwn/download_playlist.html", {"videos":videos,"link":"value="+url})
        else:
            return redirect("playlist")
        
    
    def post(self, request):
        videos = request.session.get("videos", False)
        if videos:
            download = []
            for k,v in request.POST.items():
                if k.startswith('video'):
                    video_no = int(k.replace('video',''))
                    stream_no = int(request.POST.get("stream"+str(video_no)))
                    download.append({
                        "video_no":video_no,
                        "stream_no":stream_no,
                        "filename":videos[video_no-1]["streams"][stream_no-1]["default_filename"],
                        "url":videos[video_no-1]["streams"][stream_no-1]["url"],
                        "resolution":videos[video_no-1]["streams"][stream_no-1]["resolution"],
                        "format":videos[video_no-1]["streams"][stream_no-1]["mime_type"]
                    })
            
            return render(request, "dwn/download_list.html", {"downloads":download})
        else:
            return redirect("playlist")