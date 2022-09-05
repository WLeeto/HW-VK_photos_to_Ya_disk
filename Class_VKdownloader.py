import requests


class VKdownloader:
    def __init__(self, token):
        self.token = token
        self.url = 'http://api.vk.com/method/'

    def get_photos(self, count=5):
        '''
        Загружает фото с профиля, возвращает json c результатами
        :param count: Количество требуемых результатов
        '''
        url = self.url + 'photos.get'
        params = {
            "access_token": self.token,
            "album_id": "profile",
            "v": "5.131",
            "extended": "1",
            "count": count
        }
        resp = requests.get(url, params=params)

        return resp.json()

    def __try_it(self):
        url = self.url + 'users.get'
        params = {
            "user_ids": "1",
            "access_token": self.token,
            "v": "5.131",
        }
        resp = requests.get(url, params=params)

        return resp.json()
