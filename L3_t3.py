import requests

class TestHeader:
    def test_get_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        r = requests.get(url)
        header = r.headers
        print(header)

        assert r.status_code == 200, "Wrong code"
        assert "x-secret-homework-header" in header, "Header is not correct"
        assert header["x-secret-homework-header"] == "Some secret value", "Header value not found"