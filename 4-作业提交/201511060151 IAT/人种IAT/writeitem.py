#生成inquisit<item>

import os

work_dir = "C:/Users/Szh/Desktop/人种IAT/image/"

os.getcwd()

os.chdir(work_dir)
picturename = os.listdir(work_dir + "white\\")

print("<item targetA>")
for i in range(0,len(picturename)):
    j = i+1
    print('    '+'/'+str(j)+' = '+'"'+'image/'+'white'+'/'+picturename[i]+'"')
print("</item>")
print("\n")


os.chdir(work_dir)
picturename = os.listdir(work_dir + "black\\")

print("<item targetB>")
for i in range(0,len(picturename)):
    j = i+1
    print('    '+'/'+str(j)+' = '+'"'+'image/'+'black'+'/'+picturename[i]+'"')
print("</item>")
print("\n")
