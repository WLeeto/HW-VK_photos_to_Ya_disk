from Class_VKdownloader import VKdownloader
from Class_YaUploader import YaUploader
from pprint import pprint
import json


class Interface:
    def __init__(self, token_vk, token_ya):
        self.token_vk = token_vk
        self.token_ya = token_ya

    def is_number(self):
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

    def greetings(self):
        print(f'{" * " * 5} Вас приветствует курсовая Марченко Олега {" * " * 5}\n'
              f'{" * " * 5} Этот скрипт позволяет выгружать фото с VK на Ya диск {" * " * 5}\n'
              f'{" * " * 5}\n'
              f'Перед началом работы убедитесь что фаилы с токенами корректно заполнены\n'
              f'Также обратите внимание что для работы с google drive вам потребуется фаил авторизации client_secrets.json '
              f'в корневом каталоге\n'
              f'')

    def help(self):
        print('Ya - резервное копирование на яндекс диск\n' 
              'G - резервное копирование на гугл диск\n' 
              'L - вывести список {id: имя} всех альбомов\n' 
              'H - вывод справки')

    def if_stream_name(self, arg):
        try:
            int(arg)
        except ValueError:
            name = VKdownloader(self.token_vk)
            name = name.resolve_name(arg)
            return name
        else:
            return arg

    def Ya_command(self):
        photos = VKdownloader(self.token_vk)
        upload = YaUploader(self.token_ya)

        owner_id = input('Введите id или stream_name пользователя, у кого стырим фотки: ')
        owner_id = self.if_stream_name(owner_id)

        print('Введите id альбома из которого будем копировать фотографии\n'
              'Для копирования фото из профиля введите profile: ')
        album_id = self.is_number()

        for i in photos.albums_list(owner_id=owner_id):
            if str(i) == album_id or album_id == 'profile':
                break
        else:
            print(f'Альбома с id {album_id} не существует')
            exit(0)

        print('Введите количество фотографий, которые будем копировать: ')
        count = str(self.is_number())

        folder_name = input('Введите название папки, которая будет создана на яндекс_диске: ')
        upload.create_folder(folder_name)

        photos_list = photos.photos_list(count=count, album_id=album_id, owner_id=owner_id)

        for url in photos_list['photos_list']:
            if str(photos_list["photos_list"][url][0]) in upload.file_list(folder_name):
                upload.upload_from_url(url, f'{folder_name}/{str(photos_list["photos_list"][url][0] + " " + photos_list["photos_list"][url][1])}')
            else:
                upload.upload_from_url(url, f'{folder_name}/{str(photos_list["photos_list"][url][0])}')

        print("Были скопированы следующие фаилы:")
        pprint(photos_list['json_out'])

    def G_command(self):
        print('Функция в разработке')

    def H_command(self):
        self.help()

    def L_command(self):
        owner_id = input('Введите id или stream_name пользователя, у кого стырим фотки: ')
        owner_id = self.if_stream_name(owner_id)

        target = VKdownloader(self.token_vk)
        pprint(target.albums_list(owner_id=owner_id))


if __name__ == '__main__':
    with open('Tokens/token_vk.txt') as token_file:
        token_vk = token_file.read()

    with open('Tokens/token_ya_disk.txt') as token_file:
        token_ya = token_file.read()

    interface = Interface(token_vk=token_vk, token_ya=token_ya)
    interface.greetings()
    interface.help()
    command = input('Введите команду: ')
    if command == "Ya":
        interface.Ya_command()
    elif command == "G":
        interface.G_command()
    elif command == "H":
        interface.H_command()
    elif command == "L":
        interface.L_command()
    else:
        print('Неизвестная команда')


