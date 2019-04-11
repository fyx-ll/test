# -*- coding: utf-8 -*-
'''打印樊思翔的加法表
1+1 =2 2+1 = 3 3+ 1 =4 ... 9+ 1 = 10
1+2=3 2+2=4
'''
#嵌套循环

#第一层循环
for a in range(1,10):
    #第二层循环
    for b in range(1,10):
        print("{0} + {1} = {2}".format(b,a,b+a),end='\t')
    print()
