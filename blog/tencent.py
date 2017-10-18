import json
import requests
from lxml import etree

class PositionInfo:
    def __init__(self):
        self.url = 'http://hr.tencent.com/'
        self.headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
        self.items = list()
        self.xx = tuple()
    def tencent(self):
        try:
            response = requests.get(self.url + 'position.php?&start=0#a', headers = self.headers)
            # print(response.url)
            xhtml = etree.HTML(response.text)
            nums = int(xhtml.xpath('//div[@class="pagenav"]/a[10]/text()')[0]) + 1
        except Exception as e:
            print(e)

        for n in range(1,nums):
            fullurl = self.url + "position.php?&start=" + str(10*n - 10) + "#a"
            yield fullurl

    def getData(self):
        item = {}
        fullurl = self.tencent()
        for url in fullurl:
            try:
                print('\033[1;33mCrawling ---> {} ......\033[0m'.format(url))
                rep = requests.get(url, headers = self.headers)
                xdata = etree.HTML(rep.text)
            except Exception as e:
                print(e)

            position_names = xdata.xpath('(//tr[@class="even"]| //tr[@class="odd"])/td/a/text()')
            # print(position_names)
            links = xdata.xpath('(//tr[@class="even"]| //tr[@class="odd"])/td/a/@href')
            # print(links)
            job_types = xdata.xpath('(//tr[@class="even"]| //tr[@class="odd"])/td[2]/text()')
            # print(job_types)
            people_numbers = xdata.xpath('(//tr[@class="even"]| //tr[@class="odd"])/td[3]/text()')
            # print(people_numbers)
            place = xdata.xpath('(//tr[@class="even"]| //tr[@class="odd"])/td[4]/text()')
            # print(place)
            publish_time = xdata.xpath('(//tr[@class="even"]| //tr[@class="odd"])/td[5]/text()')
            # print(publish_time)
        #
        # for idx in range(0,10):
        #     item['position_names'] = position_names[idx]
        #     # print(item['position_names'])
        #     item['links'] =  self.url + str(links[idx])
        #     item['job_types'] = job_types[idx]
        #     item['people_numbers'] = people_numbers[idx]
        #     item['place'] = place[idx]
        #     item['publish_time'] = publish_time[idx]
        #     yield item
            yield list(zip(position_names ,links ,job_types ,people_numbers ,place ,publish_time))


    def main(self):
        self.xx = ("position_names" ,"links" ,"job_types" ,"people_numbers" ,"place" ,"publish_time")
        itemdata = self.getData()
        for nn in itemdata:
            for abc in nn:
                # print(list(zip(self.xx,abc)))
                dict1 = {k:v for k,v in list(zip(self.xx,abc))}
                print(dict1)
                self.items.append(dict1)
            print(len(self.items))
        # for _ in range(0,10):
        #     # pass
        #     self.items.append(next(itemdata))
        # print(self.items)
        # for it,v in itemdata:
        #     print('{} -- > {}'.format(it,v))
        # print(len(self.items))
        line = json.dumps(self.items, ensure_ascii=False)
        with open('tenxun.json', 'wb') as t:
            t.write(line.encode('utf-8'))


if __name__ == "__main__":
    tenxun = PositionInfo()
    tenxun.main()
