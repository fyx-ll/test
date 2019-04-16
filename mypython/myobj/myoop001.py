# -*- coding: utf-8 -*-
'''定义学生类'''


class Student:  # 类名一般首字母大写，多个单词采用驼峰原则
    #python中属性必须使用构造方法"__int__"定义，self代表当前对象本身
    def __init__(self, name, score):              # self 必须位于第一个参数单词是 init 不是int
        self.name = name
        self.score = score

    def say_score(self):  # self 必须是位于第一个参数。
        print('{0}的分数是：{1}'.format(self.name, self.score))

print(type(Student)) #类型对象，也可以理解为模具
print(id(Student))
s1 = Student('fanwei', 98)
print('s1类型', type(s1))
print('s1的id', id(s1))

s1.say_score()
s1.score = 90
s1.age = 35
print(s1.age) #新加的属性，在s2中是没有的
print(s1.score) #修改的属性

s2 = Student('abc', 100)
print('s2类型', type(s2))
print('s2的id', id(s2))
print(s2.score)