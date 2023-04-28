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


def Upload(file_data,file_name,user_name,file_mimetype):
    SCOPES=["https://www.googleapis.com/auth/drive"]
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

    folder_name = user_name
    try:
        service = build("drive","v3",credentials=creds)
        response = service.files().list(q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'",spaces='drive').execute()
        if not response['files']:
            file_metadata={
                "name" : folder_name,
                "mimeType" : "application/vnd.google-apps.folder"
            }
            file = service.files().create(body=file_metadata,fields = "id").execute()
            folder_id = file.get("id")
        else:
            folder_id = response['files'][0]["id"]
        file_metadata={
            "name" : file_name,
            "parents" : [folder_id]
        }
        media = MediaIoBaseUpload(io.BytesIO(file_data), mimetype=file_mimetype)
        upload_file=service.files().create(body = file_metadata,media_body=media,fields = "id").execute()
        print(f"FILE UPLOADED TO GOOGLE DRIVE {upload_file.get('id')}")
        return upload_file.get("id")

    except HttpError as ex:
        print(str(ex))



def HashFile():
    pass