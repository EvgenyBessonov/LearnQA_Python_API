# print ("Hello from Evgeny")

import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

