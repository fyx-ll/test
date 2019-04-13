# -*- coding: utf-8 -*-
'''测试可变参数处理（元组和字典两种方式）'''

#一个星号，元组的处理方式
def f1(a, b, *c):
    print(a, b, c)
    print(c) #*c是一个元组
    print(type(c))

f1(1, 2, 3, 4)



def f2(a, b, **c):
    print(a, b, c)
    print(c)
    print(type(c))

#f2(1,2,3,4) 此时必须传入字典

f2(1, 2, name ='abc', age = 18 )

def f3(a, b, *c, **d):
    print(a, b, c, d)
    print(c)
    print(type(c))
    print(d)
    print(type(d))

f3(1,2,3,4, t1 = 5,t2 = 6)


'''强制命名参数测试'''

def f4(*a, b, c):
    print(a,b,c)
    print(a)
    print(type(a))

#f4(1,2,3,4) 会报错。由于a是可变参数，将2,3,4全部收集，造成b 和 c 没有赋值。
f4(1,2,b=3,c=4) #强制命名