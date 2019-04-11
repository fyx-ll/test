# -*- coding: utf-8 -*-
'''练习绘制同心圆'''
#用到了海龟库

import turtle

#定义一个比对象
pen = turtle.Pen()
#绘制圆形,海龟绘制的圆形是以起点处开始绘制一个传入值为半径的圆。
#因此绘制同心圆需要绘制一个圆后，需要回到初始圆心处使用goto() 命令

pen.circle(40)
pen.up()
pen.goto(0,-20)
pen.down()
pen.circle(60)
pen.penup()
pen.goto(0,-40)
pen.pendown()
pen.circle(80)
#重置turtle位置
#pen.reset()

#绘制完成后窗口进入等待状态。
turtle.done()