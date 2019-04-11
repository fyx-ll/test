# -*- coding: utf-8 -*-
'''练习绘制同心圆'''
# 用到了海龟库

import turtle
import random
#海龟绘制同心圆
#设置x = 0，y= -（半径c2 - 半径c1）坐标，
x = 0
y = 0
c1 = 0
col = ['red','black','green','blue','yellow']
turtle.pensize(4)
turtle.hideturtle()
turtle.speed(6)
for c in range(1, 11):
    #定义半径
    c2 = c*10
    #定义goto移动的x，y坐标值
    y = -c2
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.color(random.choice(col),random.choice(col))
    #turtle.begin_fill() # 填充开始
    turtle.circle(c2)
    #turtle.end_fill()  # 填充结束

#绘制完成后窗口进入等待状态。
turtle.done()
#绘制
