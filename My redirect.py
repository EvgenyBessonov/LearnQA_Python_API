import requests

r = requests.get('https://playground.learnqa.ru/api/long_redirect')     # r = response

print("Прошло {} редиректа".format(len(r.history)))
print("Итоговый URL: {}".format(r.url))





















