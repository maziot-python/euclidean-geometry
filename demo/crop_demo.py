# -*-coding:utf-8-*-
from PIL import Image

original_image = Image.open("01-01.png")
original_width, original_height = original_image.size
print(original_width, original_height)

x1 = 40
y1 = 125
x2 = 1040
y2 = 1875
cropped_image = original_image.crop((x1, y1, x2, y2))

height = y2 - y1
width = int(height / 480 * 800)
background = Image.new('RGB', (width, height), '#C0C0C0')

x3 = (width - (x2 - x1)) // 2
background.paste(cropped_image, (x3, 0))
background.save("crop.png")

