import requests
import pytest

class TestUserAgent:
    data = [
        ({
            "user_agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "platform": "Mobile",
            "browser": "No",
            "device": "Android"}),
        ({
            "user_agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
            "platform": "Mobile",
            "browser": "Chrome",
            "device": "iOS"}),
        ({
            "user_agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "platform": "Googlebot",
            "browser": "Unknown",
            "device": "Unknown"}),
        ({
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
            "platform": "Web",
            "browser": "Chrome",
            "device": "No"}),
        ({
            "user_agent":"Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "platform": "Mobile",
            "browser": "No",
            "device": "iPhone"})
    ]

    @pytest.mark.parametrize("data", data)
    def test_user(self, data):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        user_agent = data["user_agent"]

        r = requests.get(url, headers={"User-Agent": user_agent})

        assert data["platform"] == r.json()["platform"], "Wrong platform from response data. Expected "+str(data["platform"])+", actual = "+str(r.json()["platform"])+"."
        assert data["browser"] == r.json()["browser"], "Wrong browser from response data. Expected "+str(data["browser"])+", actual = "+str(r.json()["browser"])+"."
        assert data["device"] == r.json()["device"], "Wrong device from response data. Expected "+str(data["device"])+", actual = "+str(r.json()["device"])+"."
