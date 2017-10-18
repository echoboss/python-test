from bs4  import BeautifulSoup
import urllib.request
url = 'http://hr.tencent.com/'
request = urllib.request.Request(url + 'position.php?&start=10#a')

response = urllib.request.urlopen(request)

resHtml = response.read()

html = BeautifulSoup(resHtml,'lxml')

result = html.select('tr[class="even"]')

print(result)
print(len(result))
result2 = html.select('tr[class="odd"]')

print(result2)
print(len(result2))
result += result2
print('分割线'.center(50,'*'))
print(result)
print(result[0].select('td a')[0].get_text())