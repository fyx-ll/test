# -*- coding: utf-8 -*-
class Person:

    def __init__(self, name):
        self.name = name

    #重写__str__方法
    def __str__(self):
        return '名字是{}'.format(self.name)


p = Person('fanwei')

print(p)    #重写前的调用<__main__.Person object at 0x0000017DA9773358>