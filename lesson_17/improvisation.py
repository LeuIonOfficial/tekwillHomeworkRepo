import requests

response = requests.get("https://api.github.com/users/python")
content = response.content
try:
    print(content)
except Exception:
    print("No internet connectivity.")