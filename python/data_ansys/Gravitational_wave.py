# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 00:00:47 2020

@author: 71769
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

#arr1,arr0=np.loadtxt('D:/python/data_ansys/wf_template.txt',dtype=np.float,delimiter=' ',unpack=True)
#plt.plot(arr1,arr0)
#plt.show()

rate_h, hstrain=wavfile.read(r'D:/python/data_ansys/H1_Strain.wav','rb')
rate_l, lstrain = wavfile.read(r'D:/python/data_ansys/L1_Strain.wav','rb')
reftime, ref_H1=np.genfromtxt(r'wf_template.txt').transpose()

htime_interval = 1/rate_h 
ltime_interval = 1/rate_l 
fig = plt.figure(figsize=(12, 6)) # 丢失信号起始点 

htime_len = hstrain.shape[0]/rate_h 
htime = np.arange(-htime_len/2, htime_len/2 , htime_interval) 
plth = fig.add_subplot(221) 
plth.plot(htime, hstrain, 'y') 
plth.set_xlabel('Time (seconds)') 
plth.set_ylabel('H1 Strain') 
plth.set_title('H1 Strain') 

ltime_len = lstrain.shape[0]/rate_l 
ltime = np.arange(-ltime_len/2, ltime_len/2 , ltime_interval) 
pltl = fig.add_subplot(222) 
pltl.plot(ltime, lstrain, 'g') 
pltl.set_xlabel('Time (seconds)') 
pltl.set_ylabel('L1 Strain') 
pltl.set_title('L1 Strain') 

pltref = fig.add_subplot(212) 
pltref.plot(reftime, ref_H1) 
pltref.set_xlabel('Time (seconds)') 
pltref.set_ylabel('Template Strain') 
pltref.set_title('Template') 
fig.tight_layout() 
plt.savefig("Gravitational_Waves_Original.png") 
plt.show() 
plt.close(fig)