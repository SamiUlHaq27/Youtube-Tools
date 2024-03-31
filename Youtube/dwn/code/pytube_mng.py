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
    str_time = f"{hours}:{minutes}:{seconds}"
    return str_time