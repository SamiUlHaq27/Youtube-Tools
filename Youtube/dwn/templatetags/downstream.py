from django import template


register = template.Library()

def getformat(mime_type:str):
    f = mime_type.split("/")
    return f[-1]
register.simple_tag(getformat)