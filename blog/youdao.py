import urllib.request
import urllib.parse
import time
import hashlib

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

timestamp = str(time.time()).replace('.', '')[:13]




if __name__ == '__main__':
    kw = input('请输入需要翻译得内容: ')
    fromdata = {
        "i": kw,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": timestamp,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "true"
    }
    print(hashlib.md5(fromdata).hexdigest())
    print(fromdata['i'])
    data = urllib.parse.urlencode(fromdata).encode('utf-8')
    print(data)
    request = urllib.request.Request(url, data=data, headers=header)
    response = urllib.request.urlopen(request)

    print(response.read())