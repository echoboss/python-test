import urllib.request
import urllib.parse

url = "https://movie.douban.com/j/new_search_subjects?"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

formdata = {
    'sort':'T',
    'range':'0,10',
    'tags':'',
    'start':'40'
}


data = urllib.parse.urlencode(formdata)

request = urllib.request.Request(url, data=data.encode('utf-8'), headers=headers)

response = urllib.request.urlopen(request)


with open('douban.json', 'wb') as dou:
    dou.write(response.read())

print(response.read().decode('utf-8'))