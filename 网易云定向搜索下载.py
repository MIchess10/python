# -*- coding: utf-8 -*-
import requests
import os
import json
import urllib

formdta = {
'params': 'HfQDvfuyBFXR5jxKye/HB/fGvjZwVH79YNXU3OwITKXw2ZM/NenoXz1GRA900afq7G2UcImTtu9YMK0xfVGtFmMSktu9o0BQhyTK5I6aHrRl44y88DkTUDiVrQG6KK83+PUfEfHQNiPWziL4ozfT71ahcW1CxP/AtC8KekgHc6AgBWLkf8idD00t8YnTFrQxUVN0NG84cgvQvrgQ96BoBhpetX5BDILzQBWQUaJBI5tqAQUk3cN+zR/S/lybwwUh8Cg26QH4dspOEVKAlrYUgA',
'encSecKey' : 'e00bbe630b3c8a956f5faf46a9313d70befa8a205220f590b696c9f5239bc6968bd3c4af4a1cd00c82b2a3f1a2d26e8e6fb238085128c71e4ba47bd801e68d7f34db86000c4d6692eaf062ca26ac8a7bad972c9ae091111a1058492c99d1a001ab3edb9cf654b3f9011874a12b81c71f1e87dc14631261e9b2f7cc38e155642d'
}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}

def getformdata() :

    return formdta

def getjsons(url,formdata) :
    try :
        r = requests.post(url,data=formdta,headers=headers,timeout=30)
        r.raise_for_status();
        r.encoding = r.apparent_encoding
        return r.text
    except :
        return  "爬取失败"

def getsongs(jsons) :
    jsdir = json.loads(jsons)
    songs = jsdir['result']['songs']
    return songs

def downmuisc(id,name) :
    url = "http://music.163.com/song/media/outer/url?id="+str(id)+".mp3"
    path = "./music/"+name+".mp3"
    if os.path.exists("./muisc") == True:
        os.mkdir("./music")
    urllib.request.urlretrieve(url,path)


def main() :
    serch = "你好"
    url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
    jsons = getjsons(url,formdta)
    songs = getsongs(jsons)
    for i in range(len(songs)) :
        id = songs[i]['id']
        name = songs[i]['name']
        print("正在下载： "+name+".mp3")
        downmuisc(id,name)
    print("下载完成")


main()
