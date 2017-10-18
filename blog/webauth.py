import requests

auth = ('echo', 'iphone')

response = requests.get('http://pro.fahai.com', auth=auth)

print(response.text)
with open('pro.html', 'wb') as pro:
    pro.write(response.text.encode('utf-8'))
print(response.content)
print(response.url)
print(response.encoding)
print(response.status_code)