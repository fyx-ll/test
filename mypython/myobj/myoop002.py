# -*- coding: utf-8 _-*-
'''测试类对象的生成'''
class Student:
    pass # 空语句

print(type(Student))
print(id(Student))

Stu1 = Student
Stu2 = Student
s1 = Stu1
s2 = Stu2
print(s1, type(s1), id(s1))
print(s2, type(s2), id(s2))
print(Stu1, type(Stu1), id(Stu1))
print(Stu2, type(Stu2), id(Stu2))