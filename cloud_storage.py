import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_files(self,file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f= open(file_from , 'rb')

        dbx.files_upload(f.read(), file_to)

def main():
    access_token='sl.A4rAW2svUb4zMYrm6Xg2HlKMjIgHrbDXePpQ9iytaZdKGBMLefzRN7ayDQNj_hInM8cl84VdVOoAzFXukN_1mmFxImS7psyEWTbEp1JXi9c5ueBYHFYCg5pSmJhZ9bDnOgJIloI'
    transfer_data=TransferData(access_token)
    file_from=input("enter the name of the file you wish to backup.")
    file_to=input("enter the full path to upload to dropbox.")

    transfer_data.upload_files(file_from, file_to)
    print("file has been moved to dropbox successfully!")

main()
