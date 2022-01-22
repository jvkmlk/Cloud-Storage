import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = '2cEZIWMmIuIAAAAAAAAAAaT1pbUwC4KXbpjL3VJWd4Fa5yeHWmfU3hQzuFFgSXIG'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to be transfer : -")
    file_to = input("Enter the full file path to be upload to dropbox:- ") 

    transferData.upload_file(file_from, file_to)
    print("The File Has Benn Uploaded")

main()