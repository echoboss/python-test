import urllib.request

http_header = urllib.request.HTTPHandler(debuglevel=1)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

opener = urllib.request.build_opener(http_header)

request = urllib.request.Request('http://baidu.com', headers=headers)
# request = urllib.request.Request('http://baidu.com')
response = opener.open(request)


print(response.read())