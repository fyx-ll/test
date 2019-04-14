# -*- coding: utf-8 -*-
'''嵌套函数，在函数内部定义的函数'''

def f1():
    print('f1() running...')

    def f2():
        print('f2() running...')

    f2()

f1()

print('---------分割线------------')
'''使用嵌套函数避免重复代码'''
#定义了两个函数
def printChineseName(name, familyName):
    print("{0} {1}".format(familyName, name))

def printEnglishName(name, familyName):
    print("{0} {1}".format(name, familyName))

#调用测试
printChineseName('薇', '樊')

printEnglishName('薇', '樊')

print('---------分割线------------')
#使用嵌套函数定义
def printName(isChinese, name, familyName):
    #函数内部的函数
    def inner_print(a, b):
        print("{0} {1}".format(a, b))
    #调用内部的函数
    if isChinese: #判断传入的值是否为真，
        inner_print(familyName, name)
    else:
        inner_print(name, familyName)

#调用测试

printName(True, '薇', '樊')

printName(False, '薇', '樊')

print('==========')
printName(1, '薇', '樊')

printName(0, '薇', '樊')
