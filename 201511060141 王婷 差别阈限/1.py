from PIL import Image
from numpy import *
import os

workdir="/Users/apple/Desktop/差别阈限"

im=array(Image.open(workdir + "love.jpg").covert('L'))
for i in range(0,16):
    j = i * 5
    im2 = im + j
    pic_im2 = Image.fromarray(im2)
    pic_im3 = pic_im2.resize((700,500))
    pic_im3.save(workdir+"gray\\"+str(j/5)+".jpg")
    PicName = os.listdir(workdir + "gray\\")

    print("<item grey>")
    for i in range(1, len(PicName)):
        print('  ' + '/' + str(i) + ' = ' + '"' + PicName[i] + '"')
    print("</item>")
    print("\n")