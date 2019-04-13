# -*- coding: utf-8 -*-
'''测试不可变的参数传递是浅拷贝'''

a = (1, 2, [10, 20])
def func001(m):
    print('m', id(m))
    m[2][0] = 30
    print(m)
    print('m',id(m))


print('a',id(a))
print(a)

#调用函数
func001(a)

print('a', id(a))
print(a)