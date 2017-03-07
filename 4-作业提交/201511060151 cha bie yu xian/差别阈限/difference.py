#批量生成不同灰度的刺激图片

from PIL import Image
from matplotlib import pylab
from pylab import *
import os

work_dir="C:/Users/Szh/Desktop/差别阈限/"

im = array(Image.open('test.jpg').convert('L'))
im = 0.5*im + 50

for i in range(1,17):
    im = im + 3
    image = Image.fromarray(uint8(im)).resize((480,300))
    image.save(work_dir + "GreyImage" + str(i-1) + ".jpg")

