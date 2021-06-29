import requests
import time

from Token import seconds

test_url = "https://playground.learnqa.ru/ajax/api/longtime_job"

# task 1
r1 = requests.get(test_url)
token = r1.json()["token"]
print(r1.status_code, r1.text)

# task 2
payload = {"token": token}
r2 = requests.get(test_url, params=payload)
assert r2.json()["status"] == "Job is NOT ready"
print(r2.status_code)

# task 3
time.sleep(r1.json()["seconds"])

# task 4
payload = {"token": token}
r3 = requests.get(test_url, params=payload)
assert r3.json()["status"] == "Job is ready"
assert "result" in r3.json()



