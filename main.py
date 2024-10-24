import requests

response = requests.get('https://github.com/Durak2000/infotask')
print(response.status_code)
print(response.text)