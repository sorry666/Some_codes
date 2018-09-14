# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:47:21 2018

@author: sorry

绘制箱型图：
箱型图是一种用作显示一组数据分散情况的统计图
上边缘，上四分位数，中位数，下四分位数。下边缘，异常值

"""


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)
data = np.random.normal(size=(1000,4),loc = 0,scale = 1)  #创建100*4个数组

labels = ['A','B','C','D']

plt.boxplot(data,labels=labels,sym='o',whis=1.5)  #sym.调整异常值显示形状，whis可以用来调整异常值显示多少

plt.show()



