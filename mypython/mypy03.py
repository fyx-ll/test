# -*- coding: uft-8 -*-
# -*- coding: utf-8 -*-

"""
测试join()函数拼接字符串和用字符串拼接符号“+”两种方法的效率
"""
import time
#使用"+"拼接字符串

start_time = time.time()
a = ''
for i in range(10000000):
    a = a+'a'
end_time = time.time()
print(end_time - start_time)

#使用join拼接
start_time1 = time.time()
b = []
for i in range(10000000):
    b.append('b')  #给列表从最后一位添加值
c=''.join(b)
end_time1 = time.time()
print(end_time1 - start_time1)