import pytube

"""
Progressive streams have both audio and video codec but not high quality
Adaptive streams split audio and video and provides high quality
"""

def get_object(link):
    return pytube.YouTube(link)

def get_streams(obj:pytube.YouTube):
    return obj.streams

def download_stream(stream:pytube.Stream):
    stream.download()

def get_captions(obj:pytube.YouTube, language_code:str):
    caption = obj.captions.get_by_language_code(language_code)
    return caption.generate_srt_captions()

def get_length(obj:pytube.YouTube) -> str:
    seconds = obj.length
    hours = int(seconds/(60*60))
    seconds = seconds%(60*60)
    minutes = int(seconds/60)
    seconds = seconds%60
    
    if seconds < 10:
        seconds = "0"+str(seconds)
    if minutes < 10:
        minutes = "0"+str(minutes)
    if hours < 10:
        hours = "0"+str(hours)
    
    str_time = f"{hours}:{minutes}:{seconds}"
    return str_time

def get_playlist(url):
    return pytube.Playlist(url)

def get_videos_data(videos):
    data = []
    for video in videos:
        data.append({
            "title":video.title,
            "description":video.description,
            "length":video.length,
            "thumbnail_url":video.thumbnail_url,
            "url":video.watch_url,
        })
        
    return data

def get_streams_data(video:pytube.YouTube):
    streams = get_streams(video)
    data = []
    for stream in streams:
        data.append({
            "itag":stream.itag,
            "url":stream.url,
            "default_filename":stream.default_filename,
            "filesize_mb":stream.filesize_mb,
            "includes_audio_track":stream.includes_audio_track,
            "includes_video_track":stream.includes_video_track,
            "mime_type":stream.mime_type,
            "resolution":stream.resolution,
        })
    return data
    