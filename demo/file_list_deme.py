# -*- coding:utf-8 -*-
import os

path = './'
files = os.listdir(path)

for file_name in files:
    if file_name.endswith(".png"):
        print(file_name)