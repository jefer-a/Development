
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


#plt.plot([1,5],[3,4],label='text')
#plt.xlabel('汉字')
#plt.ylabel('Y')
#plt.show()

# ax,fi=plt.subplots()
# fi.plot(10*np.random.randn(100),10*np.random.randn(100),'o')
# fi.set_title('text')
# plt.show()
theta = np.linspace(0.0,2*np.pi,10)   
r=np.random.randint(0,10,10)
plt.polar(theta,r)
plt.show()



# with open("D:\\python\\text_script\\1.txt",'r') as txt:
#     data=txt.readlines()
#     sums=sum(float(i) for i in data)
# print(sums)


#1-100加法
# count=5
# index=1
# sums=0
# while index<=5:
#     sums=sums+index
#     index=index+2
#     print(sums,index)
# print(sums)
# for i in range(1,11,5):
#     print('qe',i,sums)
#     sums=sums+i
#     print(i,sums)
# print(sums)



# 加法程序：
# x=input('x:')
# y=int(input('y:'))
# z=x+y
# print(type(x))
# print(type(y))

# 一元二次方程求解：
# a=int(input('a的值：'))
# b=int(input("b:"))
# c=int(input('c:'))
# derta=b**2-(4*a*c)
# if derta>0:
#     x1=(-b+derta**0.5)/(2*a)
#     x2=(-b-derta**0.5)/(2*a)
#     print('x1=',x1)
#     print('x2=',x2)
# elif derta==0:
#     x=(-b)/(2*a)
#     print('x1,x2=',x)
# else:
#     print("x无实数解")
#     x1=(-b+derta**0.5)/(2*a)
#     x2=(-b-derta**0.5)/(2*a)
#     print('x1=',x1)
#     print('x2=',x2)
#     print(type(x1))