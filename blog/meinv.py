import requests
from bs4 import BeautifulSoup

url = "http://www.mzitu.com/"
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
          "Referer": "http://www.mzitu.com/",
          }

#
# response = requests.get(url, headers=header)
# html = response.text
# soup = BeautifulSoup(html, features='html.parser')
# print(soup)
# nums = soup.find_all('a', class_="page_numbers")
# print(nums)
# pages = int(nums[-2].text)
# print(pages)
# print(soup)
# print(response.text)
# print(response.url)
#
#
# html = requests.get('http://www.mzitu.com/105279/2', headers=header)
# print(html.text)


url2='http://i.meizitu.net/2017/10/12b04.jpg'

response = requests.get(url2, headers=header).content

with open('hei.jpg','wb') as img:
    img.write(response)

