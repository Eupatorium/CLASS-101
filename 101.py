import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

    def main():
        access_token = 'sl.AvmTToi2_HzotqL6i83cndEN9tKTZ_w3GALPj7OoFEuM3_U0sr5xQ9vHZ3t6dnH9nBdM70mltbZ7tDftzjRb5kBcZFi3srrtogBkFVRxdATX_Iz5SmASMiJD6v25I9ayRn1kzU'
        TransferData = TransferData(access_token)
        file_from = input("enter the file path to transfer")
        file_to = input("enter the full path to upload to dropbox")
        TransferData.upload_file(file_from, file_to)
        print("file has been moved")
        
    main()