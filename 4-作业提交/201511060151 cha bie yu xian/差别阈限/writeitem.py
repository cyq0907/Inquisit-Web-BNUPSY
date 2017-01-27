#生成iquisit<item>

import os

work_dir="C:/Users/Szh/Desktop/差别阈限/Image/"

PicName = os.listdir(work_dir)
print("<item pic>")
j = 0
for i in range(0,len(PicName)-1):
        j = i+1
        print('    ' + '/' + str(j) + ' ' + '=' + ' ' + '"' + PicName[j] + '"')
print("</item>")
print("\n")
