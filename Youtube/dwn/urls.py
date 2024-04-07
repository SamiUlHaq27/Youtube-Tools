from django.urls import path
from .import views

urlpatterns = [
    path('', views.Video.as_view(), name="home"),
    path('playlist/', views.Playlist.as_view(), name="playlist"),
    path('playlist/download', views.PlaylistDownload.as_view(), name="playlist_download"),
]
