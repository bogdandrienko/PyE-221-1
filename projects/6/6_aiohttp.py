import asyncio

import requests
import os
import concurrent.futures
import aiohttp


class FileAlreadyExists(Exception):
    def __init__(self, text: str):
        self.error_text = text

    def get_error(self) -> str:
        return self.error_text


def get_name(file_name="pic.jpg"):
    response = requests.get(url="https://picsum.photos/600/600/", headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

                            )

    try:
        if os.path.exists(file_name):
            raise FileAlreadyExists("File already exists! ")
        file = open(file_name, "wb")
        file.write(response.content)
    except FileAlreadyExists as error:
        os.remove(file_name)
        print(f"Файл уже есть! {error.get_error()}")
        get_name("pic2.jpg")
    except Exception as error:
        print(error)
    finally:
        # file.close()
        pass


def multi():
    current_thread = 16
    with concurrent.futures.ThreadPoolExecutor(max_workers=current_thread * 2 + 1) as executor:
        for x in range(1, 10 + 1):
            executor.submit(get_name, f'img{x}.jpg')


async def multi_async():
    await asyncio.gather(*[get_name_async(f"img{i}.jpg") for i in range(1, 10 + 1)])


async def get_name_async(file_name: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://picsum.photos/600/600/", headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }

                               ) as request:
            response = await request.read()

    with open(file_name, "wb") as file:
        file.write(response)


def async_start():
    asyncio.run(multi_async())


if __name__ == '__main__':
    # get_name()
    # multi()
    async_start()