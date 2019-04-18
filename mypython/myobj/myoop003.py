# -*- coding: utf-8 _-*-
'''类属性的使用测试'''

class Student:

    company = 'ABC' #类属性
    count = 0

    def __init__(self, name, score):
        self.name = name                #实例属性
        self.score = score
        Student.count = Student.count+1 #每创建一个对象，count +1,相当于对象的计数器

    def say_score(self):
        print("公司是：", Student.company)
        print(self.name,'分数是：',self.score)

print(id(Student))
s1 = Student('fanwei', 90) #s1是实例对象，自动调用__init__()方法
s1.say_score()
print('一共创建{0}个Student对象'.format(Student.count))
print(id(s1))
s2 = Student('fanwei01', 80) #s2是实例对象，自动调用__init__()方法
s2.say_score()
print('一共创建{0}个Student对象'.format(Student.count))
print(id(s2))