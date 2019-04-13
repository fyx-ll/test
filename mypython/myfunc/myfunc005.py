# -*- coding: utf-8 -*-
'''测试全局变量和局部变量的效率问题'''

import math
import time
from math import sqrt

def func01():
    '''定义函数func01，调用该函数时，会调用全局变量math.sqrt'''
    start = time.time()
    for i in range(1, 100000000):
        math.sqrt(i)
    end = time.time()
    print('耗时：{0}'.format(end - start))

def func02():
    '''定义函数func02，调用该函数时，会调用局部变量b '''
    b = math.sqrt #局部变量b直接引用math.sqrt函数的地址
    start = time.time()
    for i in range(1, 100000000):
        b(i)
    end = time.time()
    print('耗时：{0}'.format(end - start))

def func03():
    '''定义函数func04，调用该函数时，会调用全局变量sqrt'''
    start = time.time()
    for i in range(1, 100000000):
        sqrt(i)
    end = time.time()
    print('耗时：{0}'.format(end - start))

def func04():
    '''定义函数func02，调用该函数时，会调用局部变量b '''
    b = sqrt #局部变量b直接引用math.sqrt函数的地址
    start = time.time()
    for i in range(1, 100000000):
        b(i)
    end = time.time()
    print('耗时：{0}'.format(end - start))

#01直接导入math模块，使用全局变量的方式调用math.sqrt()函数
func01()
#02直接导入math模块，使用局部变量的方式调用b = math.sqrt函数
func02()
#03仅仅导入math模块的sqrt函数，使用全局变量的方式调用sqrt()函数
func03()
#04仅仅导入math模块的sqrt函数，使用局部变量的方式调用b = sqrt()函数
func04()

'''结论： 1.整体导入一个模块是很耗时间的，应该用什么模块的函数等就导入什么模块
         2.全局变量的使用会影响性能，但是并不是不能使用全局变量。'''
