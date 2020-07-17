# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:14:44 2020

@author: 71769
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


#plt.plot([1,5],[3,4],label='text')
#plt.xlabel('汉字')
#plt.ylabel('Y')
#plt.show()

ax,fi=plt.subplots()
fi.plot(10*np.random.randn(100),10*np.random.randn(100),'o')
fi.set_title('text')
plt.show()
theta = np.linspace(0.0,2*np.pi,10)   
r=np.random.randint(0,10,10)
plt.polar(theta,r)
plt.show()
