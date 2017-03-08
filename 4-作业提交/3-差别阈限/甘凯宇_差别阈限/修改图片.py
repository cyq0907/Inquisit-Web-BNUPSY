from PIL import Image
from PIL import ImageDraw

#工作目录
work_dir = "C:\yuxian"
#图片名
sti_img = Image.open('thFC0SBWJL.jpg').convert('L')
draw = ImageDraw.Draw(sti_img)
for x in range(17):
     for i in range(0, list(sti_img.size)[0]):
            for j in range(0, list(sti_img.size)[1]):
                    color = sti_img.getpixel((i, j))
                    color = color + x
                    point = [i,j]
                    draw.point(point, color)
                    picture_name = work_dir + "\dipic" + str(x) + ".jpg"
     sti_img.save(picture_name)
