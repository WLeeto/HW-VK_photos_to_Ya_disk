import requests
from datetime import datetime


class VKdownloader:
    def __init__(self, token):
        self.token = token
        self.url = 'http://api.vk.com/method/'
        self.version = '5.131'

    def get_photos(self, count=5, album_id='profile'):
        '''
        Загружает фото с профиля, возвращает json c результатами
        :count: Количество требуемых результатов
        :album_id: Название альбома (по умолчанию фото профиля)
        '''
        url = self.url + 'photos.get'
        params = {
            "access_token": self.token,
            "album_id": album_id,
            "v": self.version,
            "extended": "1",
            "count": count
        }
        resp = requests.get(url, params=params)
        return resp.json()

    def get_albums(self):
        url = self.url + 'photos.getAlbums'
        params = {
            "access_token": self.token,
            "v": self.version,
        }
        resp = requests.get(url, params=params)
        return resp.json()

    def photos_list(self):
        photos_list = {}
        json_out = []
        for j in self.get_photos()["response"]["items"]:
            for i in j['sizes']:
                if i['type'] == 'z':
                    photos_list[i['url']] = [str(j["likes"]["count"]),
                                             datetime.utcfromtimestamp(j["date"]).strftime('%Y-%m-%d')]
                    json_out.append({"file_name": str(j["likes"]["count"])
                                                              + " " +
                                                              datetime.utcfromtimestamp(j["date"]).strftime('%Y-%m-%d'), "size": i['type']})

        return {"photos_list": photos_list,
                "json_out": json_out}

