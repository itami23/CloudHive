from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload , MediaIoBaseUpload
import os
import os.path
from io import BytesIO
import io
from .functions import *

# class FileUpload(View):
#     def get(self,request,*args,**kwargs):
#         form = FileForm()
#         context = {
#             'form' : form,
#         }
#         return render(request,"ChApp/file-upload.html",context)

#     def post(self,request,*args,**kwargs):
#         SCOPES=["https://www.googleapis.com/auth/drive"]
#         form = FileForm(request.POST,request.FILES)
#         if form.is_valid():
#             f = form.save(commit=False)
#             f.user = request.user
#             f.file_hash = "deeezzzzznuuuuttttssss"

#             file_name = form.cleaned_data["title"]
#             uploaded_file = request.FILES['file']
#             file_data = request.FILES['file'].read()
            
#             creds = None
#             if os.path.exists('token.json'):
#                 creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#             if not creds or not creds.valid:
#                 if creds and creds.expired and creds.refresh_token:
#                     creds.refresh(Request())
#                 else:
#                     flow = InstalledAppFlow.from_client_secrets_file("ChApp/creds.json",SCOPES)
#                     creds = flow.run_local_server(port=0)
#                 with open('token.json', 'w') as token:
#                     token.write(creds.to_json())

#             folder_name = request.user.username
#             try:
#                 service = build("drive","v3",credentials=creds)
#                 response = service.files().list(q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'",spaces='drive').execute()
#                 if not response['files']:
#                     file_metadata={
#                         "name" : folder_name,
#                         "mimeType" : "application/vnd.google-apps.folder"
#                     }
#                     file = service.files().create(body=file_metadata,fields = "id").execute()
#                     folder_id = file.get("id")
#                 else:
#                     folder_id = response['files'][0]["id"]
#                 file_metadata={
#                     "name" : file_name,
#                     "parents" : [folder_id]
#                 }
#                 media = MediaIoBaseUpload(io.BytesIO(file_data), mimetype=uploaded_file.content_type)
#                 upload_file=service.files().create(body = file_metadata,media_body=media,fields = "id").execute()
#                 print(f"FILE UPLOADED TO GOOGLE DRIVE {upload_file.get('id')}")
#                 f.file_id = upload_file.get("id")
#                 f.save()
#             except HttpError as ex:
#                 print(str(ex))

           
#             return redirect("home")

        
#         return render(request,"ChApp/file-upload.html")







class FileUpload(View):
    def get(self,request,*args,**kwargs):
        form = FileForm()
        context = {
            'form' : form,
        }
        return render(request,"ChApp/file-upload.html",context)

    def post(self,request,*args,**kwargs):
        
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.file_hash = "deeezzzzznuuuuttttssss"

            file_name = form.cleaned_data["title"]
            uploaded_file = request.FILES['file']
            filename, file_extension = os.path.splitext(uploaded_file.name)
            a = file_name+file_extension
            file_data = request.FILES['file'].read()
            
            upload_file = Upload(file_data,a,request.user.username,uploaded_file.content_type)
            
            f.file_id = upload_file
            f.save()
            
            return redirect("home")
        
        return render(request,"ChApp/file-upload.html")