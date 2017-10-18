
import urllib.request


url = 'http://baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

html = response.read()

data = html.decode('utf-8')
print(type(data))

with open('baidu.html', 'w') as baidufile:
    baidufile.write(str(data))
