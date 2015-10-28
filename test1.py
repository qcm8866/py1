import requests
url = requests.get('http://www.baidu.com')
print(url.text)