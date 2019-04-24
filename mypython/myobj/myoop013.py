# -*- coding: utf-8 -*-
'''测试继承'''

class Person:

    def __init__(self, name, age):
        self.name = name
        #self.__age = age              #私有属性
        self.age = age

    def say_age(self):
        print('{0}的年龄是{1}。'.format(self.name, self.age))
        #print("年龄是私有属性，不能显示")

    #父类方法
    def say_introduce(self):
        print('我的名字是{0}'.format(self.name))

class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age) #定义子类时，必须在其构造函数中调用父类的构造函数,必须显式的调用不然解释不会调用父类
        self.score = score

    #方法的重写,重写父类的方法
    def say_introduce(self):
        print('我的名字是{0}，年龄是{1}'.format(self.name, self.age))


print(Student.mro()) #打印类的层次

s = Student('fanwei', 35, 90)

s.say_age()

s.say_introduce() #重写父类的方法代码后调用子类的方法代码
#print(s._Person__age) #打印私有的属性