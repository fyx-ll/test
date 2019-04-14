# -*- coding: utf-8 -*-
'''测试nonlocal ，global 关键字的用法'''

a = 100 #定义全局变量 global a

#定义外层测试嵌套函数
def outer():
    b = 10 # 定义了外层函数的b nonlocal
    #定义内层测试函数
    def inner():
        nonlocal b  #声明外部函数的局部变量，不改变值时是只读是不用声明的，但是涉及到改变时必须先声明
        global a    #声明全局变量，规则和nonlocal一样，改值就要声明
        print('全局变量a：', a)
        print('本函数的外层变量b：', b)
        b = 20
        a = 200
    #调用内存嵌套函数
    inner()

    print('外层表量b：', b)

outer()
print('全局变量a：', a)
