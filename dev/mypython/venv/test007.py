# -*- coding: utf-8 -*-
'''嵌套循环效率测试'''

import time

start_time = time.time()
for a in range(1000):
    result=[]
    for b in range(10000):
        result.append(a*1000 + b*100)
end_time = time.time()
print('耗时：{0}'.format(end_time - start_time))

print('=======分割线==========')
start_time1 = time.time()
for c in range(1000):
    result1 = []
    e = c*1000
    for d in range(10000):
        result.append(c+d*100)
end_time1= time.time()
print('耗时：{0}'.format(end_time1 - start_time1))