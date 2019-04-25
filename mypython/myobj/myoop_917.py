# -*- coding: utf-8 -*-
'''测试多态'''

class Man:
    def eat(self):
        print("饿了就要吃饭")

class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭")

class English(Man):
    def eat(self):
        print("英国人用叉子吃饭")

class Indian(Man):
    def eat(self):
        print("印度人用右手吃饭")


def manEat(m):
    if isinstance(m, Man): #如果传入的类型是Man的子类，一个方法的调用，根据对象不同调用不同方法。 这就是多态
        m.eat()
    else:
        print("不能吃饭")

class A:
    pass

manEat(Chinese())

manEat(English())

manEat(Indian())

manEat(Man())

manEat(A())

