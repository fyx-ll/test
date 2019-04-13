# -*- coding: utf-8 -*-
'''测试浅拷贝和深拷贝'''

from copy import copy, deepcopy

#测试前拷贝

def testCopy():
    a = [10, 20, [1, 2]]
    b = copy(a)
    print('a', id(a))
    print('b', id(b))
    print('a', a)
    print('b', b)
    #修改b的值
    b.append(30)
    b[2].append(3)
    #检查结果
    print('---浅拷贝分割线---')
    print('a', id(a))
    print('b', id(b))
    print('a', a)
    print('b', b)

def testDeepcopy():
    a = [10, 20, [1, 2]]
    b = deepcopy(a)
    print('a', id(a))
    print('b', id(b))
    print('a', a)
    print('b', b)
    #修改b的值
    b.append(30)
    b[2].append(3)
    #检查结果
    print('---深拷贝分割线---')
    print('a', id(a))
    print('b', id(b))
    print('a', a)
    print('b', b)


testCopy()

print('=======================')

testDeepcopy()