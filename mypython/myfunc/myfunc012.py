# -*- coding: utf-8 -*-
'''测试递归函数,需要注意
1.终止条件，使递归不在自己调用自己
2.递归步骤，满足条件自己调用自己
'''

#使用递归函数计算阶乘（factorial）

def factorial(n):
    if n > 1: #递归条件
        return n*factorial(n-1) #自己调用自己
    else:      #终止条件
        return 1 #不在调用自己

#写法3，附带执行流程
def factorial2(n):
    if n == 1: #终止条件
        return 1  #不在调用自己
    #递归条件只要不等于
    #print('{0} * {1}'.format(n, n-1))
    return n*factorial2(n-1) #自己调用自己

#写法2
def factorial1(n):
    if n == 1: #终止条件
        return 1  #不在调用自己
    else:          #递归条件
        #print('{0} * {1}'.format(n, n-1))
        return n*factorial1(n-1)  #自己调用自己


print('写法1')
for i in range(1, 6):
    print('{0}! = {1}'.format(i, factorial(i)))

print('写法3')
for i in range(1, 6):
    print('{0}! = {1}'.format(i, factorial2(i)))

print('写法2')
for i in range(1, 6):
    print('{0}! = {1}'.format(i, factorial1(i)))



print('=======分割线===========')
def test01(n):
    print('test01:', n)
    if n == 0:
        print('over')
    else:
        test01(n-1)
    print('test01***', n)

test01(4)

