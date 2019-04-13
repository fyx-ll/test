# -*- coding: utf-8 -*-
'''函数可变对象参数传递测试'''

b = [1, 2, 3]
def func01(m):
    print('m的id为：{0}'.format(id(m))) #b 和 m 是同一个对象
    m.append(4) #由于m 是可变对象，不创建对象的拷贝，直接修改这个对象
    print(m)
    print('m的id为：{0}'.format(id(m)))

#调用函数func01
print('b的id为：{0}'.format(id(b)))
func01(b)
print('b的id为：{0}'.format(id(b)))
print(b)
print('-------------分割线----------------------')
'''函数不可变对象参数传递测试'''
a = (1, 2, 3)

def func02(n):
    print('n的id为：{0}'.format(id(n))) #a 和 n 是同一个对象
    n = n + (4, )  #由于a是不可变对象，因此创建一个新的对象n
    print(n)
    print('n的id为：{0}'.format(id(n))) #此时n指向了新的引用地址

#调用函数func02
print('a的id为：{0}'.format(id(a)))
func02(a)
print('a的id为：{0}'.format(id(a))) #a仍然指向了原来的引用。
print(a)