import re
import requests
from lxml import etree



headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1","Referer":"http://m.mm131.com/"}

url = "http://m.mm131.com/more.php?page=1"

# response = requests.get(url,headers=headers)
qipao = requests.get('http://m.mm131.com/qingchun/',headers=headers)
qipao.encoding = qipao.apparent_encoding
idx = requests.get('http://m.mm131.com/',headers=headers)
idx.encoding = idx.apparent_encoding
xhtm = etree.HTML(idx.text)
idx_list = xhtm.xpath('//li[@class="dropdown"]/ul/li/a/@href')
print(idx_list)
for idx_url in idx_list:
    rep = requests.get(idx_url,headers=headers)
    rep.encoding = rep.apparent_encoding
    xrep = etree.HTML(rep.text)
    all_nums = xrep.xpath('//span[@id="spn"]/text()')
    for nums in all_nums:
        com = re.compile(r'/(\d+)')
        page_list = com.findall(nums)
        print(page_list)
# print(qipao.text)
pic = re.compile(r'(http:[^\s]*?.html)')
# print(set(pic.findall(qipao.text)))
# print(response.text)