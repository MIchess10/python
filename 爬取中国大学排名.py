import requests
from bs4 import BeautifulSoup
import bs4

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}

def getHtmlText(url) :

    try :
        r = requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except :
        return ("爬取失败！")

def fillUlist(ulist,html) :
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children :
        if isinstance(tr,bs4.element.Tag) :
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUlist(ulist) :
    print("{}{}{}".format('排名','学校','得分'))
    for i in range(20) :
        u=ulist[i]
        print("{:^3}{:^10}{:^3}".format(u[0],u[1],u[2]))

def main() :
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    uifo = []
    html = getHtmlText(url)
    fillUlist(uifo,html)
    printUlist(uifo)

main()
