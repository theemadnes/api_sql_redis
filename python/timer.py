import requests

while True:
    print(requests.get("http://127.0.0.1:5000/v1/messages").elapsed.total_seconds())
    print(requests.get("http://127.0.0.1:5000/v1/users").elapsed.total_seconds())
    print(requests.get("http://127.0.0.1:5000/v1/jobs").elapsed.total_seconds())
    print(requests.get("http://127.0.0.1:5000/v1/messages/detail").elapsed.total_seconds())
