import urllib.request


httpproxy_header = urllib.request.ProxyHandler({"http":"139.59.125.77:443"})

nullproxy_header = urllib.request.ProxyHandler({})
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

proxySwitch = True

if proxySwitch:
    opener = urllib.request.build_opener(httpproxy_header)
else:
    opener = urllib.request.build_opener(nullproxy_header)


request = urllib.request.Request("http://baidu.com", headers=headers)

response = opener.open(request)

print(response.read())

