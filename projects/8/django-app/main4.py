import requests
import aiohttp
import random
import math
import cmath
import cv2
import numpy as np

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
# data = {"name": "Python is awesome"}
# response = requests.post(
#     url="http://127.0.0.1:8000/test2/",
#     data=data,
#     headers=headers,
# )
# text = "python"
# response = requests.get(
#     url=f"http://127.0.0.1:8000/test2/?text={text}&area=154",
#     params=data,
#     headers=headers,
# )
# print(response)
# print(response.status_code)
# print(response.content)  # b'\x0f\x0e\x0e\x0e\x0e\x0e\x0e'.decode()
# print(response.text)
# print(response.json())

url = "https://picsum.photos/1920/1080/"
response = requests.get(
    url=url,
    headers=headers,
)
image_data = response.content
name = f"temp/image{random.randint(1, 1000000)}.jpg"

with open(name, "wb") as opened_file:
    opened_file.write(image_data)


# https://tproger.ru/translations/opencv-python-guide/
# https://habr.com/ru/post/528144/

# str1 = "Python is awesome"
# print(str1[0:-4:1])

image_data = cv2.imread(name, 0)
# image_data = cv2.resize(image_data, (400, 400))
# image_data = image_data
# im_resize = cv2.resize(image_data, None, fx=1.0, fy=1.0)
# cv2.imwrite(path, image)
#                                   x1 y1   x2  y2

# image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)

def encode_image(data):
    # resize inserted image
    data = cv2.resize(data, (1920, 1080))
    # run a color convert:
    data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
    return bytes(data)  # encode Numpay to Bytes string


def decode_image(data):
    # Gives us 1d array
    decoded = np.fromstring(data, dtype=np.uint8)
    # We have to convert it into (270, 480,3) in order to see as an image
    # decoded = decoded.reshape((1920, 1080, 3))
    # return decoded
    # return cv2.imdecode(decoded, cv2.IMREAD_COLOR )


# image_data = decode_image(image_data)
image_data = cv2.cvtColor(image_data, cv2.COLOR_RGB2BGR)
gray_image = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
# ret, threshold_image = cv2.threshold(image_data, 127, 255, 0)
# cv2.imshow("gray_image", gray_image)
# cv2.imshow("image_data", image_data[10:600, 50:750])
# cv2.imshow("threshold_image", threshold_image)
# cv2.waitKey(0)
cv2.imwrite("temp/new_image.jpg", image_data)
