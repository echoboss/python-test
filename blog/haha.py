import os
import re
import sys
import urllib.request



print('\033[1;32m Starting ! \033[0m'.center(50, '*'))

destdir = os.path.abspath('')

def Destfile(path):
    if not os.path.isdir(destdir):
        os.mkdir(destdir)
    pos = path.rindex('/')
    localpath =  os.path.join(destdir, path[pos+1:])
    return localpath


if __name__ == "__main__":
    url = 'http://pic.yesky.com/c/6_3655.shtml'
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    data = response.read()
    a = set(re.findall(r'(http:[^\s]*?(jpg|png|gif))', str(data)))
    print(a)
    # for link, t in set(re.findall(r'(http:[^\s]*?(jpg|png|gif))', str(data))):
    #     print('{} ----> {}'.format(link, t))
    #     try:
    #         urllib.request.urlretrieve(link, Destfile(link))
    #         print('OK ---> {}'.format(link))
    #
    #     except:
    #         print('failde')

    print('\033[1;32m Stoping ! \033[0m'.center(50, '*'))