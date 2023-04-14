from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def get_images():
  gauth = GoogleAuth()
  gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
  drive = GoogleDrive(gauth)
    
  address_proof_file = drive.CreateFile({'id':'17VUJ0TgnSXyujaw2mmyiJrGAuP4nSgXy'})
  address_proof_file.GetContentFile('image_data/sample_address_proof.png')

  address_proof_file = drive.CreateFile({'id':'1hpt8Pa5SbUCM7JpB8eglH_UU19m83-kk'})
  address_proof_file.GetContentFile('image_data/sample_id.png')

if __name__ == '__main__':
    get_images()