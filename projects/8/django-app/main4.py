import requests
import aiohttp
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
data = {"name": "Python is awesome"}
# response = requests.post(
#     url="http://127.0.0.1:8000/test2/",
#     data=data,
#     headers=headers,
# )
text = "python"
response = requests.get(
    url=f"http://127.0.0.1:8000/test2/?text={text}&area=154",
    params=data,
    headers=headers,
)
print(response)
print(response.status_code)
print(response.content)  # b'\x0f\x0e\x0e\x0e\x0e\x0e\x0e'.decode()
print(response.text)
