
import requests
import pprint
from tqdm import tqdm
import time


class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}


    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def photos_info(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, 'album_id': 'profile', 'count': 5, 'extended': 1}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def long_function():
        for i in tqdm(range(100)):
            time.sleep(0.1)
        return True

    #def save_fotos(self):
        #response = requests.get(imageUrl)
        #with open ('image.jpg', 'wb') as f:
            #f.write(response.content)
            #filename = 'imageUrl'.split('/')[-1]



access_token = 'vk1.a.LZk2iRKfBk-ZwOEm9laeHk'
user_id = '23193179'
vk = VK(access_token, user_id)

pprint.pprint(vk.photos_info())

class YD_connector:

    def __init__(self, token):
        self.headers = {'Authorization': f'OAuth {token}'}
        token = 'y0_AgAAAABgrLWwAAA'

    def create_folder(self, folder_name):
        url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'

        response = requests.put(url_create_folder,
                                headers=self.headers,
                                params={'path': folder_name})
        return response.status_code

    def up_load_image(self):
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload')
        url = 'https://sun9-25.userapi.com/impf/c622216/v622216179/59ba/TsAYkjuqWaI.jpg?size=682x1024&quality=96&sign=736129f06efaa4ea86d5dc6dbff76475&type=album'
        params = 'https://disk.yandex.ru/client/disk/folder_name'


