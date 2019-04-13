# -*- coding: utf-8 -*-
'''测试函数的定义和调用'''

#有返回值得函数
def func01():
    print('hello world!')
    return '世界，你好！'

#没有返回值得函数
def func02():
    print('good luck!')

#直接调用
func01()
func02()
print('------分割线-------')

#直接调用并使用返回值
print(func01())
print(func02())
#多次调用
print('------分割线-------')
for _ in range(2):
    print(func01())
    print(func02())