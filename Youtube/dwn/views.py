from django.shortcuts import render
from .code import pytube_mng
from Youtube.settings import BASE_DIR

"""https://youtu.be/aM9-zFvH6kI?si=JQ5uOV27NeM5JwZW"""
def home(request):
    main_url = request.GET.get("url")
    if(main_url != None):
        streams = pytube_mng.get_streams(pytube_mng.get_object(main_url))
        request.session["url"] = main_url
    else:
        streams = []
    return render(request, "home.html", {"streams":streams})

def download(request, itag):
    print("itag = ",itag)
    url = request.session.get("url")
    streams = pytube_mng.get_streams(pytube_mng.get_object(url))
    stream = streams.get_by_itag(itag)
    path = stream.download(output_path=BASE_DIR/'media'/'output', filename=stream.default_filename)
    path = "/home/sami/Code/Youtube-Tools/Youtube/media/output/Allama Khadim Hussain Rizvi  Man Ashiq E Sar Mastam  Ghazi Ilm Deen Shaheed  Poetry.mp4"
    return render(request, "download.html", {"link":path.split("/")[-1]})
