# -*- coding: utf-8 -*-
'''复利计算函数'''

#复利 本利和=本金(1+利息)**时期



def func_s(a, b, c):
    p = a
    i = b
    n = c
    if n > 0:
        s = p * (1 + i) ** n
        #print('{0}的复利是{1}'.format(n, s))
        return s+func_s(a,b,c-1)
    else:
        return 0




p = 6000 #本金
i = 0.07   #利息
n = 20    #时期
s = func_s(p,i,n)
print(s)
print(20*6000)