# -*- coding: utf-8 -*-
'''@property 装饰器的用法'''

class Employee:

    def __init__(self, name, salary):
        self.__name = name      #私有方法
        self.__salary = salary  #私有方法

    # python 通过装饰器的写法
    @property  # 实现get方法，把方法当做是属性，只能看不能修改
    def salary(self):
        return self.__salary

    @salary.setter  # 通过装饰器修饰过的setter方法来修改属性
    def salary(self, salary):
        if 1000 < salary < 300000:
            self.__salary = salary
        else:
            print('输入错误，{0}不在1000--300000之间'.format(salary))


''' #类似java的写法 set，get 方法
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if 1000< salary <300000:
            self.__salary = salary
        else:
            print('输入错误，{0}不在1000--300000之间'.format(salary))
'''



e = Employee('fanwei', 20000)

print(dir(e))
print('------------------------------------')
#python装饰器的写法的调用

print(e.salary)  #调用 get
e.salary = 2000  #设置 set
print(e.salary)  #调用
e.salary = -2000  #设置 set
print(e.salary)  #调用

''' #类似java的写法的调用
print(e.get_salary())
e.set_salary(2000)
print(e.get_salary())
e.set_salary(-2000)  #输入值不在范围，修改失败，值不变
print(e.get_salary())
'''
