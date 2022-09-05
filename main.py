from Class_VKdownloader import VKdownloader
from Class_YaUploader import YaUploader
from datetime import datetime
from pprint import pprint

if __name__ == "__main__":

    with open('Tokens/token_vk.txt') as token_file:
        token_vk = token_file.read()

    photos = VKdownloader(token_vk)
    photos_list = {}
    json_out = []
    for j in photos.get_photos()["response"]["items"]:
        for i in j['sizes']:
            if i['type'] == 'z':
                photos_list[i['url']] = [str(j["likes"]["count"]),
                                         datetime.utcfromtimestamp(j["date"]).strftime('%Y-%m-%d')]
                json_out.append({"file_name": str(j["likes"]["count"])
                                              + " " +
                                              datetime.utcfromtimestamp(j["date"]).strftime('%Y-%m-%d'), "size": i['type']})

    with open('Tokens/token_ya_disk.txt') as token_file:
        token_ya = token_file.read()

    upload = YaUploader(token_ya)
    folder_name = 'Homework_Marchenko'
    upload.create_folder(folder_name)
    for url in photos_list:
        upload.upload_from_url(url, f'{folder_name}/{str(photos_list[url][0] + " " + photos_list[url][1])}')

    pprint(json_out)
