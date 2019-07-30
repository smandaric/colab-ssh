import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials, ApplicationDefaultCredentialsError

def copy_keys(drive_folder='ssh'):
    # Create ssh folder
    if not os.path.exists('/root/.ssh'):
        os.makedirs('/root/.ssh')

    # Authenticate Google Drive
    gauth = GoogleAuth()

    try:
        gauth.credentials = GoogleCredentials.get_application_default()
    except ApplicationDefaultCredentialsError:
        auth.authenticate_user()
        gauth.credentials = GoogleCredentials.get_application_default()

    drive = GoogleDrive(gauth)
    
    #Copy all files in Drive folder
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false and mimeType='application/vnd.google-apps.folder' and title='{}'".format(drive_folder)}).GetList()
    assert len(file_list) == 1
    
    ssh_folder_id = file_list[0]['id']
    ssh_file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(ssh_folder_id)}).GetList()

    for ssh_file in ssh_file_list:
        ssh_file.GetContentFile('/root/.ssh/{}'.format(ssh_file['title']))
        print('Copied file /root/.ssh/{}'.format(ssh_file['title']))
