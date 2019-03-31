# -*- coding: utf-8 -*-
'''练习1：定义多点坐标,绘制折线,并计算起始点和终点的距离'''
#导入模块
import turtle
import math

#定义4个点的坐标
x1, y1 = 100, 100
x2, y2 = 100, -100
x3, y3 = -100, -100
x4, y4 = -100, 100

#使用turtle绘制

turtle.penup()          #抬起画笔
turtle.goto(x1, y1)    #画笔移动到指定位置
turtle.pendown()        #放下画笔开始画线
turtle.goto(x2, y2)
turtle.goto(x3, y3)
turtle.goto(x4, y4)

#计算两点间的距离，使用math模块,公式为 (x1-x2)**2+(y1-y2)**2,然后开方
distance = math.sqrt((x1-x4)**2+(y1-y4)**2)
turtle.write(distance)
