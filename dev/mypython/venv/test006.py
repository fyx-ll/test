# -*- coding：utf-8 -*-
'''测试while循环及break和continue的用法'''
a = 0
while a <= 10:
    if  a % 2 == 0:
        print('even_num :{0}'.format(a))
    else:
        break
    a += 1
print('end')

b = 0
while b<=10:
    if b%2 == 0 :
        print('even_num :{0}'.format(b))
    b = b+1
    continue
print('end2')