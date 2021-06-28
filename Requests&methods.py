import requests

test_url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

print("# 1 Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае")
r = requests.get(test_url)
print(r.status_code, r.text)

print("# 2 Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае")
payload = {'method': 'HEAD'}
r = requests.head(test_url, data=payload)
print(r.status_code, r.text)

print("# 3 Делает запрос с правильным значением method. Описать что будет выводиться в этом случае")
payload = {'method': 'GET'}
r = requests.get(test_url, params=payload)
print(r.status_code, r.text)

print("# 4 С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method."
      "Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее."
      "И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок")

methods = ["GET", "POST", "PUT", "DELETE"]

for api_method in methods:
    for params_method in methods:
        if api_method == "GET":
            r = requests.request(api_method, test_url, params={"method": params_method})
        else:
            r = requests.request(api_method, test_url, data={"method": params_method})
