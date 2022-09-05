import requests


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

    def __try_it(self):
        '''
        Просто тест, не лезьте
        '''
        url = self.url + 'users.get'
        params = {
            "user_ids": "1",
            "access_token": self.token,
            "v": self.version,
        }
        resp = requests.get(url, params=params)

        return resp.json()
