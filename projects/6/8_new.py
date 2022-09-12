import requests
import aiohttp
import asyncio
import re

url = "https://jsonplaceholder.typicode.com/photos/"
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
data = requests.get(url=url, headers=headers, timeout=5.0)

photos = data.json()
# print(photos)

# [
#   {
#     "albumId": 1,
#     "id": 1,
#     "title": "accusamus beatae ad facilis cum similique qui sunt",
#     "url": "https://via.placeholder.com/600/92c952",
#     "thumbnailUrl": "https://via.placeholder.com/150/92c952"
#   }

class Photo:
    def __init__(self, albumId: int, id: int, title: str, url: str, thumbnailUrl: str):
        self.albumId = albumId
        self._id = id
        self._title = title
        self._url = url
        self._thumbnailUrl = thumbnailUrl

    def check_valid_url(self) -> bool:
        """Проверка валидности ссылки через регулярные выражения"""
        return len(re.findall(r'\bhttp.*?\b', self._url)) > 0

    @staticmethod
    def check_valid_url_static(url: str) -> bool:
        """Проверка валидности внешней ссылки через регулярные выражения"""
        return len(re.findall(r'\bhttp.*?\b', url)) > 0

    def __repr__(self):
        return f" | {self._id}, {self._title} | "

photo_list = []

for photo in photos:
    photo_list.append(Photo(albumId=photo['albumId'],
    id=photo['id'],
    title=photo['title'],
    url=photo['url'],
    thumbnailUrl=photo['thumbnailUrl']))

print(photo_list)

# photos = Photo(
#     albumId=photos['albumId'],
#     id=photos['id'],
#     title=photos['title'],
#     url=photos['url'],
#     thumbnailUrl=photos['thumbnailUrl']
#     )

print(Photo.check_valid_url_static(url='https://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python'))
print(Photo.check_valid_url_static(url='hps://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python'))
Photo.check_valid_url_static(url='https://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python')
# async def get_photos():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url=url, headers=headers, timeout=5.0) as response_object:
#             response = await response_object.read()
#             print(response)
#
#
# asyncio.run(get_photos())

import practice28
from practice28 import get_data
import openpyxl
workbook = openpyxl.Workbook()
worksheet = workbook.active



# load_workbook(filename = 'таблица 1-8.xlsx')
cell_coord = "E10"
worksheet[cell_coord].value = "python"
counter = 1
for photo in get_data():
    worksheet[f"A{counter}"] = photo.get_title()
    worksheet[f"C{counter}"] = photo.albumId
    counter += 1
workbook.save("new.xlsx")
workbook.close()
if __name__ == "__main__":
    data = get_data()
    print(data)

import requests
import aiohttp
import asyncio
import re

def get_data():
    url = "https://jsonplaceholder.typicode.com/photos/"
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/102.0.0.0 Safari/537.36'
            }
    data = requests.get(url=url, headers=headers, timeout=5.0)

    photos = data.json()
    # print(photos)

    # [
    #   {
    #     "albumId": 1,
    #     "id": 1,
    #     "title": "accusamus beatae ad facilis cum similique qui sunt",
    #     "url": "https://via.placeholder.com/600/92c952",
    #     "thumbnailUrl": "https://via.placeholder.com/150/92c952"
    #   }

    class Photo:
        def __init__(self, albumId: int, id: int, title: str, url: str, thumbnailUrl: str):
            self.albumId = albumId
            self._id = id
            self._title = title
            self._url = url
            self._thumbnailUrl = thumbnailUrl

        def check_valid_url(self) -> bool:
            """Проверка валидности ссылки через регулярные выражения"""
            return len(re.findall(r'\bhttp.*?\b', self._url)) > 0

        @staticmethod
        def check_valid_url_static(url: str) -> bool:
            """Проверка валидности внешней ссылки через регулярные выражения"""
            return len(re.findall(r'\bhttp.*?\b', url)) > 0

        def __repr__(self):
            return f" | {self._id}, {self._title} | "

    photo_list = []

    for photo in photos:
        photo_obj = Photo(albumId=photo['albumId'],
        id=photo['id'],
        title=photo['title'],
        url=photo['url'],
        thumbnailUrl=photo['thumbnailUrl'])
        photo_list.append(photo_obj)

    # print(photo_list)

    # photos = Photo(
    #     albumId=photos['albumId'],
    #     id=photos['id'],
    #     title=photos['title'],
    #     url=photos['url'],
    #     thumbnailUrl=photos['thumbnailUrl']
    #     )

    # print(Photo.check_valid_url_static(url='https://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python'))
    # print(Photo.check_valid_url_static(url='hps://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python'))
    # Photo.check_valid_url_static(url='https://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python')
    # async def get_photos():
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get(url=url, headers=headers, timeout=5.0) as response_object:
    #             response = await response_object.read()
    #             print(response)
    #
    #
    # asyncio.run(get_photos())
    return photo_list

if __name__ == "__main__":
    data = get_data()
    print(data)

```import requests
import aiohttp
import asyncio
import re

def get_data():
    url = "https://jsonplaceholder.typicode.com/photos/"
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/102.0.0.0 Safari/537.36'
            }
    data = requests.get(url=url, headers=headers, timeout=5.0)

    photos = data.json()
    # print(photos)

    # [
    #   {
    #     "albumId": 1,
    #     "id": 1,
    #     "title": "accusamus beatae ad facilis cum similique qui sunt",
    #     "url": "https://via.placeholder.com/600/92c952",
    #     "thumbnailUrl": "https://via.placeholder.com/150/92c952"
    #   }

    class Photo:
        def __init__(self, albumId: int, id: int, title: str, url: str, thumbnailUrl: str):
            self.albumId = albumId
            self._id = id
            self._title = title
            self._url = url
            self._thumbnailUrl = thumbnailUrl

        def check_valid_url(self) -> bool:
            """Проверка валидности ссылки через регулярные выражения"""
            return len(re.findall(r'\bhttp.*?\b', self._url)) > 0

        @staticmethod
        def check_valid_url_static(url: str) -> bool:
            """Проверка валидности внешней ссылки через регулярные выражения"""
            return len(re.findall(r'\bhttp.*?\b', url)) > 0

        def __repr__(self):
            return f" | {self._id}, {self._title} | "

    photo_list = []

    for photo in photos:
        photo_obj = Photo(albumId=photo['albumId'],
        id=photo['id'],
        title=photo['title'],
        url=photo['url'],
        thumbnailUrl=photo['thumbnailUrl'])
        photo_list.append(photo_obj)

    # print(photo_list)

    # photos = Photo(
    #     albumId=photos['albumId'],
    #     id=photos['id'],
    #     title=photos['title'],
    #     url=photos['url'],
    #     thumbnailUrl=photos['thumbnailUrl']
    #     )

    # print(Photo.check_valid_url_static(url='https://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python'))
    # print(Photo.check_valid_url_static(url='hps://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python'))
    # Photo.check_valid_url_static(url='https://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python')
    # async def get_photos():
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get(url=url, headers=headers, timeout=5.0) as response_object:
    #             response = await response_object.read()
    #             print(response)
    #
    #
    # asyncio.run(get_photos())
    return photo_list

if __name__ == "__main__":
    data = get_data()
    print(data)```