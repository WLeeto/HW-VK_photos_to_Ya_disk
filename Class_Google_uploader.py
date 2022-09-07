from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

response = GoogleAuth()
response.LocalWebserverAuth()


def create_and_upload(file_name='test.txt', file_content='Hello world!'):
    try:
        drive = GoogleDrive(response)

        my_file = drive.CreateFile(({'title': f'{file_name}'}))
        my_file.SetContentString(file_content)
        my_file.Upload()

        return f'Фаил {file_name} загружен'
    except Exception as _ex:
        return 'Что то пошло не так'


if __name__ == '__main__':
    print(create_and_upload())
