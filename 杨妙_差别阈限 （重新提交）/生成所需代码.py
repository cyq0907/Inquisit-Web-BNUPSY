# !/usr/bin/evn python
# _*_ encoding:utf-8_*_
# -*- coding: utf-8 -*-

'this is a test module'

__author__ = 'Miao Yang'

import os

work_dir = "D:\work\Python\\picture\\"

os.getcwd()

os.chdir(work_dir)

# 遍历两个需要扫描的文件夹，并将文件名导入到列表当中

NPicNames = os.listdir(work_dir+"NPic\\")

# 打印出inquisit所需要的格式

print("<item NR>")
for i in range(0, len(NPicNames)):
    j = i+1
    print('<picture'+'  '+'N'+str(j)+'>'+'\n')
    print('   '+'/'+str(j)+' = ' + '"' + NPicNames[i] + '"'+'\n')
    print("</picture>")
print("\n")

