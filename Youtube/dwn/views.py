from django.shortcuts import render, redirect
from .code import pytube_mng
from Youtube.settings import BASE_DIR
from django.views import View

"""https://youtu.be/aM9-zFvH6kI?si=JQ5uOV27NeM5JwZW"""

class home(View):
    
    url = ""
    display_error = False
    display_streams = False
    youtube_object = None
    streams = []
    
    def get(self, request):
        itag = request.GET.get("id", False)
        self.url = request.session.get("url", False)
        if itag and self.url:
            self.youtube_object = pytube_mng.get_object(self.url)
            self.streams = pytube_mng.get_streams(self.youtube_object)
            stream = self.streams.get_by_itag(itag)
            stream.download(filename=stream.default_filename, output_path=BASE_DIR/"media"/"output")
            return redirect("/media/output/"+stream.default_filename)
        return render(request, 'dwn/index.html', {"error":self.display_error})
    
    def post(self, request):
        self.url = request.POST.get("url")
        request.session["url"] = self.url
        try:
            self.youtube_object = pytube_mng.get_object(self.url)
            self.streams = pytube_mng.get_streams(self.youtube_object)
            self.display_streams = True
        except Exception as e:
            print(e)
            self.display_error = True
        return render(request, 'dwn/index.html', {
            "title":self.youtube_object.title,
            "duration":pytube_mng.get_length(self.youtube_object),
            "thumbnail":self.youtube_object.thumbnail_url,
            "description":self.youtube_object.description,
            "link":"value="+self.url,
            "error":self.display_error,
            "streams":self.streams,
            "display_streams":self.display_streams,
            })
    