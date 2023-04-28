from django.urls import path
from .views import *
urlpatterns = [
    path("upload/",FileUpload.as_view(),name='file_upload'),
    path('list/',FileList.as_view(),name="file_list"),
    path('download/<file_id>/',download_file,name='file-download'),
    path('view/<file_id>/',ViewModifyFileInfo.as_view(),name = "view-modify"),

]
