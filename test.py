import requests

Base = "http://127.0.0.1:5000/"

response = requests.get(url=Base)
print(f"{response.status_code}")