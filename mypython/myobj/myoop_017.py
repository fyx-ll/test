# -*- coding: utf-8 -*-
'''测试运算符的重载'''

class Person:

    def __init__(self, name):
        self.name = name


    def __add__(self, other):
        if isinstance(other, Person):
            return '{0} ---{1}'.format(self.name, other.name)

        else:
            return '{0}和{1}类型不同，不能相加'.format(self.name, other.name)

class A:
    def __init__(self, name):
        self.name = name


p1 = Person('fanwei')

p2 = Person('fanyuxi')

a1 = A('abc')
#重写后的方法相加
print(p1+p2)
p1.__add__(p2)

print(p1 + a1)
