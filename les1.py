import requests

# GET - ЗАПРОС ДАННЫХ
# POST - ОПУБЛИКОВАТЬ ДАННЫЕ
# PUT - ИЗМЕНИТЬ ДАННЫЕ
# PATCH - Изменить чать данные
# DELETE - Удалить данные


# url = 'https://geekbrains.ru/'
url = 'https://5ka.ru/special_offers/'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0",
}
# params = {
#     'hello': 22,
#     'first': True,
# }
response = requests.get(url, headers=headers)
print(1)
