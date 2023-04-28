from django.urls import path
from .views import *
urlpatterns = [
    path("upload/",FileUpload.as_view(),name='file_upload'),
]
