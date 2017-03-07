#来自 http://lovenight.github.io/2015/11/15/Python-3-%E5%A4%9A%E7%BA%BF%E7%A8%8B%E4%B8%8B%E8%BD%BD%E7%99%BE%E5%BA%A6%E5%9B%BE%E7%89%87%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C/

import requests
import re
import os

url = r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&sf=1&fmq=1447473655189_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=黑人'
dirpath = r'C:\Users\16005\Documents\GitHub\Inquisit-Web-BNUPSY\4-作业提交\唐莹莹_IAT'

html = requests.get(url).text
urls = re.findall(r'"objURL":"(.*?)"', html)

if not os.path.isdir(dirpath):
    os.mkdir(dirpath)

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
    if index == 6:
        break

print("下载结束，一共 %s 张图片" % index)

url = r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&sf=1&fmq=1447473655189_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=白人'
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
    if index == 6:
        break

print("下载结束，一共 %s 张图片" % index)
