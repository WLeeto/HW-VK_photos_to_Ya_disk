from Class_VKdownloader import VKdownloader
from Class_YaUploader import YaUploader
from datetime import datetime
from pprint import pprint

if __name__ == "__main__":

    with open('Tokens/token_vk.txt') as token_file:
        token_vk = token_file.read()

    photos = VKdownloader(token_vk)
    photos_list = photos.photos_list()

    with open('Tokens/token_ya_disk.txt') as token_file:
        token_ya = token_file.read()

    upload = YaUploader(token_ya)
    folder_name = 'Homework_Marchenko'
    upload.create_folder(folder_name)
    for url in photos_list['photos_list']:
        upload.upload_from_url(url, f'{folder_name}/{str(photos_list["photos_list"][url][0] + " " + photos_list["photos_list"][url][1])}')

    pprint(photos_list['json_out'])
