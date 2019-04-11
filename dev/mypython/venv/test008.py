# -*- coding: utf-8 -*-
'''测试zip()并行迭代'''
for i in [1,2,3,4]:
    print(i)

names = ['abc','def','ghi']
ages = [18,19,20]
jobs = ['123','456','789']
#zip()并行迭代
for  name,age,job in zip(names,ages,jobs):
    print('{0} - {1} - {2}'.format(name,age,job))