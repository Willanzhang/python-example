#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tesseract_py.py
@Time    :   2019/11/15 17:31:45
@Author  :   William 
@Version :   1.0
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib
from pytesseract import *
from PIL import Image

# 打开图片
image = Image.open("code.jpg")

text = image_to_string(image)

print text