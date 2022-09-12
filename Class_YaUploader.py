import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_url(self, ya_disk_file_path):
        response = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        header = self.get_header()
        params = {'path': ya_disk_file_path, 'overwrite': 'true'}
        response_get = requests.get(response, headers=header, params=params)
        return response_get.json()

    def upload_txt(self, ya_disk_file_path, filename):
        response_link = self.get_url(ya_disk_file_path=ya_disk_file_path)
        href = response_link.get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        # Проверяем сработала ли функция
        response.raise_for_status()
        if response.status_code == 201:
            print('Выполнено')

    def upload_from_url(self, url, name):
        '''
        Загружает фаил с url на ya disk
        :param url: Откуда загружать
        :param name: Путь на ya disk
        :return:
        '''
        reference = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            "path": name,
            "url": url,
        }
        response = requests.post(reference, headers=self.get_header(), params=params)
        response.raise_for_status()
        if response.status_code == 202:
            print(f'Загрузка {name} завершена')

    def create_folder(self, folder_name):
        '''
        Создает папку в корневом каталоге
        Если папка с таким именем уже есть - даст ошибку
        :param folder_name: Имя папки
        '''
        reference = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            "path": folder_name,
        }
        requests.put(reference, headers=self.get_header(), params=params)
        print(f'Папка {folder_name} создана')

    def file_list(self, folder_name):
        '''
        Получает список фаилов на диске в указанной папке
        :return:
        '''
        files_list = []
        response = 'https://cloud-api.yandex.net/v1/disk/resources'
        header = self.get_header()
        params = {
            "path": folder_name,
        }
        response_get = requests.get(response, headers=header, params=params)
        for i in response_get.json()["_embedded"]['items']:
            files_list.append(i['name'])
        return files_list


if __name__ == "__main__":
    with open('Tokens/token_ya_disk.txt') as token_file:
        token_ya = token_file.read()

    test = YaUploader(token_ya)

    pprint(test.file_list('New folder'))
