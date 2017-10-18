import urllib.parse
import urllib.request

input_wd = input('Please input some string :')

word = {'wd':input_wd}
zhcode = urllib.parse.urlencode(word)
print('\033[1;33m {} \033[0m'.format(zhcode))

print('\033[1;34m {} \033[0m'.format(urllib.request.unquote(zhcode)))


url = 'https://www.baidu.com/s?'

newurl = url + zhcode

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

request = urllib.request.Request(newurl, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))