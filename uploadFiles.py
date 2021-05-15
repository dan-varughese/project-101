import dropbox
import os



class TransferData:
    for root, dirs, files, in os.walk(file_from):
       relative_path = os.path.relpath(local_path, file_from)
       dropbox_path = os.path.join(root, relative_path)
    with open(local_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = ''
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer:')
    file_to = input('Enter the full path to upload to dropbox')

    transferData.upload_file(file_from, file_to)
    print('File has been moved')