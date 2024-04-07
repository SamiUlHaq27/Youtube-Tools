from django import template
import pytube

register = template.Library()

def getformat(mime_type:str):
    f = mime_type.split("/")
    return f[-1]
register.simple_tag(getformat)

def get_length(seconds) -> str:
    seconds = int(seconds)
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
register.simple_tag(get_length)