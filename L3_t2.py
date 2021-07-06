import requests

class TestCookie:
    def test_get_cookies(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        r = requests.get(url)
        cookies = r.cookies.get_dict()
        print(cookies)

        assert r.status_code == 200, "Wrong response code"
        assert "HomeWork" in cookies, "Cookies is not correct"
        assert cookies["HomeWork"] == "hw_value", "Cookies value not found"
