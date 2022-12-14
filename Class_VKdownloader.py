import requests
from datetime import datetime
from pprint import pprint


class VKdownloader:
    def __init__(self, token):
        self.token = token
        self.url = 'http://api.vk.com/method/'
        self.version = '5.131'

    def get_photos(self, count=5, album_id='profile', owner_id=None):
        '''
        Загружает фото с профиля, возвращает json c результатами
        :count: Количество требуемых результатов
        :album_id: Название альбома (по умолчанию фото профиля)
        '''
        url = self.url + 'photos.get'
        params = {
            "owner_id": owner_id,
            "access_token": self.token,
            "album_id": album_id,
            "v": self.version,
            "extended": "1",
            "count": count
        }
        resp = requests.get(url, params=params)
        return resp.json()

    def albums_list(self, owner_id=None):
        '''
        Возвращает словарь {'id альбома': 'название альбома'}
        '''
        url = self.url + 'photos.getAlbums'
        params = {
            "owner_id": owner_id,
            "access_token": self.token,
            "v": self.version,
        }
        album = requests.get(url, params=params).json()
        all_albums = {}
        for albums in album['response']['items']:
            all_albums[albums["id"]] = albums["title"]

        return all_albums

    def photos_list(self, count=5, album_id='profile', owner_id=None):
        '''
        Возвращает словарь {{"photos_list": {'ссылка для загрузки': 'имя для загрузки'}},
                           {"json_out": {'"file_name": 'имя фаила', "size": "размер фаила"} }}
        '''
        photos_list = {}
        json_out = []
        for j in self.get_photos(count=count, album_id=album_id, owner_id=owner_id)["response"]["items"]:
            for i in j['sizes']:
                biggest = 0
                count = i['height'] * i['width']
                if count > biggest:
                    biggest = count
            for i in j['sizes']:
                if i['height'] * i['width'] == biggest:
                    photos_list[i['url']] = [str(j["likes"]["count"]), datetime.utcfromtimestamp(j["date"]).strftime('%Y-%m-%d')]
        for i in photos_list:
                json_out.append({"file_name": photos_list[i][0] + photos_list[i][1], "size": f'{biggest} px'})
        return {"photos_list": photos_list,
                "json_out": json_out}

    def resolve_name(self, screen_name):
        url = self.url + 'utils.resolveScreenName'
        params = {
            "screen_name": screen_name,
            "v": self.version,
            "access_token": self.token
        }
        id = requests.get(url, params=params)
        return id.json()['response']['object_id']

if __name__ == '__main__':
    with open('Tokens/token_vk.txt') as token_file:
        token_vk = token_file.read()

    photos = VKdownloader(token_vk)
    pprint(photos.resolve_name("leonaland"))
