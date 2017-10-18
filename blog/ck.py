import requests

# url = 'https://baidu.com'
# url = 'http://www.renren.com/PLogin.do'
# url = 'https://i.qq.com/'
url = 'http://www.12306.cn/mormhweb/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
#
#
#
# response = requests.get(url, headers=headers)
#
# ck= response.cookies
# ckdict= requests.utils.dict_from_cookiejar(ck)
#
#
# print(ck)
#
#
# print(ckdict)


# ssion = requests.session()
#
# data = {"u": "40017612", "p": "iphone"}
#
# ssion.post(url, data=data)
#
# response = ssion.get("https://user.qzone.qq.com/3051479117")
# print(response.text)
#
# with open('heihei.html','wb') as de:
#     de.write(response.text.encode('utf-8'))



response = requests.get(url, headers=headers, verify=False)

print(response.text)