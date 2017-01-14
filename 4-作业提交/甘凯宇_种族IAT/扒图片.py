import requests
import re
import os

url = r'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%BA%DA%C8%CB&fr=ala&ori_query=%E9%BB%91%E4%BA%BA&ala=0&alatpl=sp&pos=0&hs=2&xthttps=111111'
dirpath = r'C:\IAT'

html = requests.get(url).text
urls = re.findall(r'"objURL":"(.*?)"', html)

index = 1
for url in urls:
    print("Downloading:", url)
    try:
        res = requests.get(url)
        if str(res.status_code)[0] == "4":
            print("未下载成功：", url)
            continue
    except Exception as e:
        print("未下载成功：", url)
    filename = os.path.join(dirpath, "black" + str(index) + ".jpg")
    with open(filename, 'wb') as f:
        f.write(res.content)
        index += 1
    if index == 8:
        break
print("共下载 %s 张图片" % index)

url = r'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1484371093756_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word=%E7%99%BD%E4%BA%BA'
html = requests.get(url).text
urls = re.findall(r'"objURL":"(.*?)"', html)
index = 1
for url in urls:
    print("Downloading:", url)
    try:
        res = requests.get(url)
        if str(res.status_code)[0] == "4":
            print("未下载成功：", url)
            continue
    except Exception as e:
        print("未下载成功：", url)
    filename = os.path.join(dirpath, "white" + str(index) + ".jpg")
    with open(filename, 'wb') as f:
        f.write(res.content)
        index += 1
    if index == 8:
        break
print("共下载 %s 张图片" % index)