# -*- coding: utf-8 -*-
'''测试全局变量与局部变量'''

a = 100 # 全局变量
b = 100 # 同上
#定义函数

def func1():
    global a #如果要在函数内改变全局变量的值，增加global关键字来声明
    print(a) #打印全局变量a的值
    a = 300

    b = 300  #定义局部变量b后才能使用b，否则就会报错UnboundLocalError: local variable 'b' referenced before assignment
    print(b)
    #b = 300 #由于没有global关键字所以这里的b是局部变量。

    #局部变量
    c = 1
    print(c)

    print(locals()) #函数func1里面的局部变量
    print(globals()) #脚本中的全局变量

func1()
print('-----分割线-----')
print(a)
print(b)
#print(c) #此时调用局部变量c 就会报错NameError: name 'c' is not defined