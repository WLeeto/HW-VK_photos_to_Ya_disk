from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import urllib.request

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
    url = 'https://sun1-26.userapi.com/impg/_ii1L_ZHZga1LYj-iHU4ru4L8nvqU4P2BTopMQ/DDpq2YEOalU.jpg?size=1280x720&quality=96&sign=2b8fbc49b8d45e5c25bdcb511d62eb55&c_uniq_tag=3dYQ71JDFMWxzPCz0HqFQ2iUUszCizERihzW8oobjW0&type=album'
    img = urllib.request.urlopen(url).read()
    print(type(img))
    create_and_upload('name.jpeg', img)
