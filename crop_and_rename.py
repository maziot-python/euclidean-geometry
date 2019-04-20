# -*- coding:utf-8 -*-
from PIL import Image
import os

path = './'
files = os.listdir(path)

start_string = input('请输入图片前缀:')
count = 0

for file_name in files:
    if file_name.endswith(".png"):
        original_image = Image.open(file_name)
        original_width, original_height = original_image.size

        # 仅第一次会做裁剪和增加背景动作
        if original_width == 1080:
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
            background.save(file_name)

        count = count + 1
        new_file_name = '%s%02d.png' % (start_string, count)
        print(file_name, '>>>', new_file_name)
        os.rename(file_name, new_file_name)

print('done')