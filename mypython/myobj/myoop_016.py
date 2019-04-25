# -*- coding: utf-8 -*-
'''测试多重继承和mro()'''

class A:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('A类里面的名字是', self.name)

class B(A):
    def __init__(self, name):
        self.name = name

    def say(self):
        print('B类里面的名字是', self.name)
        A.say(self)      #调用A的方法
        super().say() #通过super()方法调用父类的定义，可以理解为代码



B1 = B('FANWEI')

B1.say()


