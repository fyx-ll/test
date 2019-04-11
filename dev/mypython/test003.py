# -*- conding: utf-8 -*-
'''利用while循环打印0-10'''

#定义需要打印的变量
num = 0
while num <=10: #while 的条件表达式是当为真时执行下面的语句/语句块
    print(num, end='\t')
    num +=1 # 等价于 num = num + 1 while语句必须有能改变条件表达式的语句块。否则会进入死循环。
print("\n打印结束")

'''计算1-100之间的累加和'''
# 1+2+3+...100
#定义累加的变量
num1 = 0

#定义打印累加和的变量
sum_num1 = 0

while num1 <= 100:
    sum_num1 = num1 + sum_num1
    num1 += 1
print(sum_num1)
