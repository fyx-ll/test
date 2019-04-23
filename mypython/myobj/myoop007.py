# -*- coding: utf-8 -*-
'''测试python方法重名的情况'''

#python中没有方法的重载，定义多个同名的方法，只有最后一个有效。

class Person:


    def say_hi(self):
        print("hello!")


    def say_hi(self,name):
        print("{0},hello".format(name))

p1 = Person()

#p1.say_hi() #运行报错。TypeError: say_hi() missing 1 required positional argument: 'name'

p1.say_hi('fanwei')