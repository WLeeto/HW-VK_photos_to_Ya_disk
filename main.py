import pandas

from Class_VKdownloader import VKdownloader
from Class_YaUploader import YaUploader
from datetime import datetime
from pprint import pprint
import json


def is_number():
    while True:
        numb = input(":")
        if numb != 'profile':
            try:
                int(numb)
            except Exception:
                print('Необходимо ввести число или "profile"')
            else:
                return numb
        return numb


if __name__ == "__main__":

    with open('Tokens/token_vk.txt') as token_file:
        token_vk = token_file.read()

    with open('Tokens/token_ya_disk.txt') as token_file:
        token_ya = token_file.read()
    photos = VKdownloader(token_vk)
    upload = YaUploader(token_ya)

    print(f'{" * " * 5} Вас приветствует курсовая Марченко Олега {" * " * 5}\n'
          f'{" * " * 5} Этот скрипт позволяет выгружать фото с VK на Ya диск {" * " * 5}\n'
          f'{" * " * 5}\n'
          f'Перед началом работы убедитесь что фаилы с токенами корректно заполнены\n'
          f'Также обратите внимание что для работы с google drive вам потребуется фаил авторизации client_secrets.json '
          f'в корневом каталоге\n'
          f'')

    help_comand = 'Ya - резервное копирование на яндекс диск\n' \
                  'G - резервное копирование на гугл диск\n' \
                  'L - вывести список {id: имя} всех альбомов\n' \
                  'H - вывод справки'

    print(help_comand)
    command = input('Введите команду: ')

    if command == 'Ya':
        print('Введите id альбома из которого будем копировать фотографии\n'
              'Для копирования фото из профиля введите profile: ')
        album_id = is_number()

        for i in photos.albums_list():
            if str(i) == album_id or album_id == 'profile':
                break
        else:
            print(f'Альбома с id {album_id} не существует')
            exit(0)

        print('Введите количество фотографий, которые будем копировать: ')
        count = str(is_number())

        folder_name = input('Введите название папки, которая будет создана на яндекс_диске: ')
        upload.create_folder(folder_name)

        photos_list = photos.photos_list(count=count, album_id=album_id)
        for url in photos_list['photos_list']:
            upload.upload_from_url(url,
                                   f'{folder_name}/{str(photos_list["photos_list"][url][0] + " " + photos_list["photos_list"][url][1])}')

        print("Были скопированы следующие фаилы:")
        pprint(photos_list['json_out'])

        with open('json_out.json', mode='w', encoding='utf-8') as file:
            json.dump(photos_list['json_out'], file)

    elif command == 'G':
        print('Функция в разработке')
    elif command == 'H':
        print(help_comand)
    elif command == 'L':
        print('Список всех альбомов {id: имя}:')
        pprint(photos.albums_list())
    else:
        print('Нераспознанная команда')
