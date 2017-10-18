import urllib.request
import urllib.parse


def tiebaSpider(url, beginPage, endPage):
    for page in range(beginPage, endPage + 1):
        pn = (page-1) * 50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        htm = loadPage(fullurl)
        writeFile(htm,filename)



def loadPage(url):
    print('\033[1;33m Download OK \033[0m ---> {}'.format(url))
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    return html



def writeFile(html, filename):

    print('\033[1;33m write disk starting \033[0m ---> {}'.format(filename))
    with open(filename,'wb') as f:
        f.write(html.encode('utf-8'))

    print('\033[1;33m Finish Write !\033[0m'.center(50,'*'))



if __name__ == "__main__":
    kw = input("请输入关键词： ")
    beginPage = int(input("请输入起始页面： "))
    endPage = int(input("请输入结束页面： "))
    url = "https://tieba.baidu.com/f?"

    key = urllib.parse.urlencode({"kw":kw})
    fullurl = url + key
    tiebaSpider(url=fullurl, beginPage=beginPage, endPage=endPage)

