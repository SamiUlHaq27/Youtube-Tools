from django import template


register = template.Library()

def download_stream(stream):
    print(stream)
    return "Downloaded"