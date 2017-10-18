import requests

kw = {'wd':'美女'}
# url = 'http://baidu.com/s?'
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
formdata = {
    "type":"AUTO",
    "i":"i love python",
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}

response = requests.post(url, data=formdata, headers=header)

print(response.text)
print(response.json())
with open('baidu.html', 'wb') as bai:
    bai.write(response.text.encode('utf-8'))
print(response.content)
print(response.url)
print(response.encoding)
print(response.status_code)


