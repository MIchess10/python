import requests
import os

url = "http://img0.dili360.com/ga/M00/48/F7/wKgBy1llvmCAAQOVADC36j6n9bw622.tub.jpg"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
root = "./photo"
path = root+'/'+url.split('.')[-2]+'.jpg';
try :
    if not os.path.exists(root) :
        os.mkdir(root)
    if not os.path.exists(path) :
        r = requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        with open(path,'wb') as f :
            f.write(r.content)
            f.close()
            print("文件保存成功！")
    else :
        print("文件已经存在！")
except :
    print("爬取失败！")

