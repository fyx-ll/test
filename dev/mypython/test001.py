#-*- coding=utf-8 -*-
'''创建列表对象'''
import time
# 使用 append添加列表对象的元素
from typing import List

start_time = time.time()
a: List[int] = [1, 2, 3]
for x in range(4, 100000):
    a.append(x)
end_time = time.time()
print(end_time - start_time)

#使用 加号 “+”添加元素。
start_time = time.time()
b = [1, 2, 3]
for x in range(4, 100000):
    b = b + [x]
end_time = time.time()
print(end_time - start_time)

#使用extend 添加元素
start_time = time.time()
c = [1, 2, 3]
for x in range(4,100000):
    c.extend([x])
end_time = time.time()
print(end_time - start_time)

#使用insert 添加元素
start_time = time.time()
d = [1, 2, 3]
for x in range(4, 100000):
    #d.insert(2, x) #直接insert到最后一位和直接insert到第二位有明显区别
    d.insert(len(d) - 2, x)
end_time = time.time()
print(end_time - start_time)

#使用符号 * 添加元素 自增长不太好用乘法，简单写了下。
start_time = time.time()
e = [1,2,3]
e = e * int(100000/3)
end_time = time.time()
print(end_time - start_time)