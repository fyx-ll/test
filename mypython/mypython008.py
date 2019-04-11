# -*- coding: utf-8 -*-
'''绘制围棋9*9的横纵线'''

#导入海龟绘图
import turtle as tl
#设置初始坐标值
a = -180
b = -180
c = 360
d = 40
tl.pensize(2)
tl.hideturtle()
tl.speed(8)
tl.penup()
tl.goto(a, b)
tl.pendown()
#棋盘为横纵9*9的线，间隔为固定值设置棋盘长度及间隔长度40
#(-180,-180) (180,-180) (-180,-140) (180,-140)

#画横线
for x in range(0, 10):
    tl.pendown()
    tl.goto(c+a, x*d+b)
    tl.penup()
    tl.goto(a, (x+1)*d + b)

#画纵线，移动光标到原点
tl.penup()
tl.goto(a, b)
for y in range(0, 10):
    tl.pendown()
    tl.goto(y*d+a, c+b)
    tl.penup()
    tl.goto((y+1)*d + a, b)


tl.done()

