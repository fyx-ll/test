# -*- coding: utf-8 -*-
'''测试私有属性和私有方法'''

class Employee:

    __company = 'google'

    def __init__(self, name, age):
        self.name = name
        self.__age = age #私有属性

    def __work(self):  #私有方法
        print('好好工作！')
        print('年龄{0}'.format(self.__age)) #类的内部调用私有属性，直接使用私有属性名称
        print('公司{0}'.format(self.__company)) #类的内部调用类的私有属性
e = Employee("fanwei", 35)
#print(e.age) #调用私有属性报错 AttributeError: 'Employee' object has no attribute 'age'
#print(e.__age) #同上
#正确调用私有属性的方法
print(e._Employee__age)  #下划线+类名+双下划线+属性名

print(dir(e))

e._Employee__work()   #和上面步骤一样