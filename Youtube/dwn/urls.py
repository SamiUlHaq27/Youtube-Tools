from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('download/<itag>', views.download, name="download"),
]
