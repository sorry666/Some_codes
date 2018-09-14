# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 13:43:58 2018

@author: sorry
绘制条形图
"""

import numpy as np
import matplotlib.pyplot as plt

N=5
y=[20,10,30,25,15]
index= np.arange(N)
pl=plt.bar(left=index,height=y) #可以通过调整参数来修改条形图颜色以及宽度
  # 通过调整left=0，bottom=index，orientation='horizationtal'来绘制水平显示的条形图
  

plt.show()

"""
绘制竖直并列条形图
"""
index=np.arange(4)
sales_BJ=[52,55,63,53]
sales_SH=[44,66,55,41]

bar_width=0.3

plt.bar(index,sales_BJ,bar_width,color='b')
plt.bar(index+bar_width,sales_SH,bar_width,color='r')

plt.bar(index,sales_SH,bar_width,color='r',bottom=sales_BJ)


plt.show()

