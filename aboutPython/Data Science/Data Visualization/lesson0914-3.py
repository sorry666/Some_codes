# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:07:36 2018

@author: sorry
绘制直方图
"""

import numpy as np
import matplotlib.pyplot as plt

mu = 100 #mean of distribution
sigma = 20 # standard deviation of distribution
x = mu +sigma*np.random.randn(2000000)


p1=plt.hist(x,bins=1000,color='green',normed=True) #bins 直方图分割区间数目， normed True标准化，False,不标准化
plt.show(p1)




"""
实现双变量的直方图，利用颜色来确定分布情况
"""


xx=np.random.randn(100000)+2
yy=np.random.randn(100000)+3

p2=plt.hist2d(xx,yy,bins=2000)

plt.show(p2)