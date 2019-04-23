# -*- coding: utf-8 -*-
'''测试 @property 性质，财产'''

class Employee:

    @property
    def salary(self):
        return 30000


emp1 = Employee()
#print(emp1.salary())  #有装饰器后就可以不用后面带()。否则会报错 TypeError: 'int' object is not callable
print(emp1.salary)     #就像调用属性一样调用方法。但是不能去修改该值
print(type(emp1.salary))