# -*- coding: utf-8 -*-
'''类方法使用测试'''
'''静态方法使用测试'''

class Student:
    company = 'abcd'      #类属性

    def __init__(self, name, score ):
        self.name = name   #实例属性
        self.score = score

    @classmethod #装饰器 可以理解为特殊标记
    def printCompany(cls):
        print(cls.company)  #调用类属性
        #print(self.score)  #调用实例属性和实例方法时就会报错，因为类方法是在实例方法及属性前面创建，

    @staticmethod
    def printadd(a, b):
        #print(cls.company) #静态方法不能调用实例属性，类属性
        print('{0} + {1} = {2}'.format(a, b , a+b))

Student.printCompany()
s1 = Student('fanwei', 90)
s1.printCompany() #调用类方法
s1.printadd(1, 2) #调用静态方法




