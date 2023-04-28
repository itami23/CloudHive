from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponse,Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import *
from .models import *
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload , MediaIoBaseUpload
from googleapiclient.http import MediaIoBaseDownload
import os
import os.path
from io import BytesIO
import io
from .functions import *
from Members.models import User

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
            

            file_name = form.cleaned_data["title"]
            uploaded_file = request.FILES['file']
            filename, file_extension = os.path.splitext(uploaded_file.name)
            a = file_name+file_extension
            file_data = request.FILES['file'].read()
            f.file_hash = HashFile(file_data)
            f.title = a
            upload_file = Upload(file_data,a,request.user.username,uploaded_file.content_type)
            
            f.file_id = upload_file
            f.save()
            
            return redirect("file_list")
        
        return render(request,"ChApp/file-upload.html")





# class FileList(View):
#     def get(self, request, *args, **kwargs):
#         # Get the user's credentials from the token.json file
#         SCOPES = ['https://www.googleapis.com/auth/drive']
#         creds = None
#         if os.path.exists('token.json'):
#             creds = Credentials.from_authorized_user_file('token.json', SCOPES)

#         # Check if the credentials are valid
#         if not creds or not creds.valid:
#             # Refresh the access token if it has expired
#             if creds and creds.expired and creds.refresh_token:
#                 creds.refresh(Request())
#             else:
#                 # Ask the user to authorize the app if this is the first time they're using it
#                 flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
#                 creds = flow.run_local_server(port=0)
#             # Save the credentials for future use
#             with open('token.json', 'w') as token:
#                 token.write(creds.to_json())

#         try:
#             # Build the Google Drive API client
#             service = build('drive', 'v3', credentials=creds)

#             # Get the list of files in the user's folder
#             folder_name = request.user.username
#             folder_query = "name='{}' and mimeType='application/vnd.google-apps.folder'".format(folder_name)
#             folder_results = service.files().list(q=folder_query, fields="nextPageToken, files(id, name)").execute()
#             folder_items = folder_results.get('files', [])
#             if not folder_items:
#                 message = 'No files found.'
#             else:
#                 # Get the list of files in the user's folder
#                 file_query = "'{}' in parents".format(folder_items[0]['id'])
#                 file_results = service.files().list(q=file_query, fields="nextPageToken, files(id, name, createdTime)").execute()
#                 file_items = file_results.get('files', [])
#                 if not file_items:
#                     message = 'No files found.'
#                 else:
#                     context = {'files': file_items}
#                     return render(request, 'ChApp/file-list.html', context)

#         except HttpError as error:
#             message = 'An error occurred: %s' % error
#             context = {'message': message}
#             return render(request, 'ChApp/file-list.html', context)


# class FileList(View):
#     def get(self,request,*args,**kwargs):
#         files = ListFile(request.user.username)
#         user = request.user
#         user_files = File.objects.filter(user = user)
#         if files and user_files :
#             context = {
#                 'files' : files,
#                 'user_files' : user_files,
#             }
#             return render(request, 'ChApp/file-list.html', context)

#         else:
#             return Http404('No Files Available')

class FileList(View):
    def get(self,request,*args,**kwargs):
        user = request.user
        user_files = File.objects.filter(user = user)
        
        context = {
                'files' : user_files,
        }
        return render(request, 'ChApp/file-list.html', context)

        





def download_file(request, file_id):
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file("ChApp/creds.json",SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('drive', 'v3', credentials=creds)
        file = service.files().get(fileId=file_id).execute()
        file_name = file['name']
        file_content = service.files().get_media(fileId=file_id).execute()
        response = HttpResponse(file_content, content_type=file['mimeType'])
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    except HttpError as error:
        print(f'An error occurred: {error}')
        return Http404('File not found')





class ViewModifyFileInfo(View):
    def get(self,request,*args,**kwargs):
        file = get_object_or_404(File,file_id=self.kwargs.get('file_id'))
        form = FileModifyForm(instance=file)
        if file.user != request.user:
            return redirect('file_list')

        context = {
            'file' : file,
            'form' : form,
        }
        return render(request, 'ChApp/file-modify.html',context)


    def post(self,request,*args,**kwargs):
        file = get_object_or_404(File,file_id=self.kwargs.get('file_id'))
        form = FileModifyForm(request.POST,instance=file)
        if file.user != request.user:
            return redirect('file_list')
        if form.is_valid():
            form.save()
            return redirect('file_list')








