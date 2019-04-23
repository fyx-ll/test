# -*- coding: utf-8 -*-
''' 测试可调用方法__call__()'''

class SalaryAccount:
    '''工资计算类'''

    def __call__(self, salary):
        print("开始计算工资")
        yearSalary = salary*12
        daySalary = salary//22.5
        hourSalary = daySalary//8

        return dict(yearSalary = yearSalary, monthSalary = salary, daySalary = daySalary, hourSalary = hourSalary)

#调用工资计算类

s1 = SalaryAccount()
print(s1(14000))