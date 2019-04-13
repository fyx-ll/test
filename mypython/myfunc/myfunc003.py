# -*- coding: utf-8 -*-
'''测试返回值的基本用法'''

def addNunber(a, b):
    '''计算两个数的和，并返回两个数的和'''
    print('计算两个数的和：{0},{1},{2}'.format(a,b,(a+b)))
    return a+b

c = addNunber(10,20)
print('----分割线-----')
print(c)

#测试函数遇到return 后会结束函数
def test01():
    print(1)
    print(2)
    return
    print(3)

test01()

#测试函数需要返回多个值时，可以使用列表，元组，字典，集合

def test02(a, b, c):
    d = [a, b, c]
    return d

e = test02(1,2,3)
print(type(e))
print(e)