import re
import os
import requests
from lxml import etree
from requests import post


class Mm:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
        self.idx_patt = '//li[@class="dropdown"]/ul/li/a/@href'
        self.all_nums = '//span[@id="spn"]/text()'
        self.com = re.compile(r'/(\d+)')

    def reqs(self, links, pattern):
        response = requests.get(links, self.headers)
        response.encoding = response.apparent_encoding
        xhtm = etree.HTML(response.text)
        fullurl = xhtm.xpath(pattern)
        for da in fullurl:
            # print(da)
            yield da

    def getidx(self):
        name_patt = '//li[@class="dropdown"]/ul/li/a/text()'
        idx_lst = self.reqs(self.url, self.idx_patt)
        idx_name = self.reqs(self.url, name_patt)
        # yield list(zip(idx_nu, idx_lst))
        # for ix in idx_lst:
        #     print(ix)
        return idx_lst, idx_name

    def getnums(self):
        idx_url = self.getidx()
        # print(idx_url)
        for url in idx_url[0]:
            idx_nums = self.reqs(links=url, pattern=self.all_nums)
            for a in idx_nums:
                page_num = self.com.findall(a)
                # print(page_num[0])
                yield page_num[0]

    def geturl(self):
        num = self.getnums()
        url_type = self.getidx()
        dict1 = {k: v for k, v in list(zip(url_type[0], num))}
        dict2 = {"http://m.mm131.com/xinggan/": 6, "http://m.mm131.com/qingchun/": 1, "http://m.mm131.com/xiaohua/": 2,
                 "http://m.mm131.com/chemo/": 3, "http://m.mm131.com/qipao/": 4, "http://m.mm131.com/mingxing/": 5}
        for k, v in dict1.items():
            for ul in range(2, int(v) + 1):
                fu = k + 'list_' + str(dict2[k]) + str('_') + str(ul) + '.html'
                yield fu

    def loadurl(self):
        a_url = self.geturl()
        a_idx = self.getidx()
        meinv_patt = '//*[@id="post-1"]/div[1]/h2/a/text()'
        url_patt = '//*[@id="post-1"]/div[1]/h2/a/@href'
        # for c in a_url:
            # print(c)
        for d in a_idx[0]:
            meinv_name = self.reqs(d,pattern=meinv_patt)
            meinv_url = self.reqs(d,pattern=url_patt)
            return meinv_name, meinv_url


    def loadimg(self):
        mei_nv = self.loadurl()
        title_patt = '//div/h2[@class="mm-title"]/text()'
        frist_img = '//div[@class="post-content single-post-content"]/a/img/@src'
        img_total = '//span[@class="rw"]/text()'
        # print(mei_nv[1])

        for e in mei_nv[1]:
            meinv_title = self.reqs(e,title_patt)
            f_img = self.reqs(e,frist_img)
            i_total = self.reqs(e,img_total)
            return mei_nv, f_img, i_total

    def writeloca(self):
        mei, f, imga = self.loadimg()
        print(mei,f,imga)
        for m in mei:
            for mm in m:
                print(mm)


    def main(self):
        self.writeloca()


if __name__ == '__main__':
    url = "http://m.mm131.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
        "Referer": "http://m.mm131.com/"}

    m = Mm(url=url, headers=headers)
    m.main()
