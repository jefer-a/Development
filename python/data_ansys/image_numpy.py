# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:02:06 2020

@author: 71769
"""


import numpy as np
from PIL import Image

image_object=Image.open('D:/photo/1920_1080/f9857dad737e3a153f9b144cb293824c.jpg')
a=np.array(image_object.convert('L'))
a1=np.array(image_object)
im=Image.fromarray(a)
im.save('D:/python/data_ansys/1.jpg')


b=255-a
imb=Image.fromarray(b.astype('uint8'))
imb.save('D:/python/data_ansys/2.jpg')

b1=[255,255,255]-a1
imb1=Image.fromarray(b1.astype('uint8'))
imb1.save('D:/python/data_ansys/3.jpg')


b2=