import requests
import json

fromdata = {
    'first':'true',
    'pn':1,
    'kd':'运维工程师'
}
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
header= {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36","Referer":"https://www.lagou.com/jobs/list_java?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput="}


response = requests.get(url, data=fromdata, headers=header)
with open('java.json','w') as f:
    json.dump(response.json(),f)
print(response.json())
