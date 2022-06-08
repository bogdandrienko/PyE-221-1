import requests

# url = 'https://www.google.com/search?q=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1' \
#       '%83&rlz=1C1IXYC_ruKZ978KZ978&oq=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB&aqs=chrome.1' \
#       '.69i57j69i59j0i512l8.8912j1j7&sourceid=chrome&ie=UTF-8 '
url = 'https://docs.python.org/3/library/datetime.html'
params = {}

response = requests.get(url=url, params=params)
if response.status_code == 200:
    content = response.content
    with open(file='temp/new2.html', mode='wb') as file:
        file.write(content)
else:
    print("ошибка получения данных!")
