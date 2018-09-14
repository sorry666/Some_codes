# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:24:54 2018

@author: sorry

绘制饼状图
"""

import numpy as np
import matplotlib.pyplot as plt


labels = 'A','B','C','D'
fracs = [15,30,45,10]
plt.axes(aspect=1)  #让横纵轴比例为1，对于饼状图，可以让饼状图必成正圆，而不是椭圆

explode = [0,0.05,0,0]  #将第二个元素移出饼状图，其强调作用


plt.pie(x=fracs,labels=labels,explode=explode)  #explode 移出饼状图   shdow=True,添加阴影

plt.show()

