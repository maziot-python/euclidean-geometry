# -*- coding:utf-8 -*-
import os

path = './'
files = os.listdir(path)

start_string = input('请输入图片前缀:')

count = 0

for file_name in files:
    if file_name.endswith(".png"):
        count = count + 1
        new_file_name = '%s%02d.png' % (start_string, count)
        print(file_name, '>>>', new_file_name)
        os.rename(file_name, new_file_name)
