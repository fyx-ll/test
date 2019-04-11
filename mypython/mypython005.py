# -*- coding: utf-8 -*-
'''测试选择结构'''

num = 1
if int(num) < 10:
    print(num)

if 3: #整数表达式
    print('ok')


#列表作为条件表达式，由于为空列表，是Fasle
a = []
if a:
    print("空列表，False")

#非空字符串，是True
s = "False"
if s:
    print("非空字符串，是True")

#数值判断
c = 9
if 3<c<10:
    print("3<c<20")

if 3<c and c<10:
    print("3<c and c<20")

#布尔值
if True:
    print("True")