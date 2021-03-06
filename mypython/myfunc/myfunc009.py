# -*- coding: utf-8 -*-
'''测试参数的几种类型'''

#位置参数

def test01(a, b, c):
    print(a, b, c)

print('位置参数，多一个少一个都会报错')
test01(10, 20, 30)
test01(c=1, b=3, a=4) #直接指明参数,也就是命名参数



#默认值参数

def test02(a, b=2, c=3): #默认值参数必须位于普通位置参数的后面。
    print(a, b, c)


print('默认值参数，有默认值得参数是可选的')
test02(2, 4)
test02(2)
test02(2, 4, 5)
test02(c=1, b=2, a=3)


#命名参数
print('命名参数，直接指明每个参数的值')
test01(c=1, b=3, a=4) #直接指明参数,也就是命名参数



