# -*- coding: utf-8 -*-
'''测试推导式'''

#列表推导式
a = [x for x in range(10)]
print(a)
print(type(a))
b = [x for x in range(10) if x%2 == 0]
print(b)
print(type(b))
#组合
ab= [[x,y] for x in range(5) for y in range(5) if x%2==0 and y%2==1]
print(ab)
print(type(ab))
#字典推导式
c = {x:y for x in range(12) for y in range(12)}
print(c)
print(type(c))
#实际应用：计算文本中字符出现的次数。
my_text = 'abcd,abcd,aac d,e f g'
char_ccount = {d:my_text.count(d) for d in my_text}
print(char_ccount)
print(type(char_ccount))
#集合表达式
e = {x*2 for x in [1,2,3] }
print(e)
print(type(e))

f = {x*2 for x in  range(10) if x<5 }
print(f)
print(type(f))

#生成器推导式 -- 生成元组
g = (x*2 for x in range(5))
print(g)
for x in g:
    print(x)
print(type(g))
for x in g:
    print('第二次调用生成器推导式{0}'.format(x))

print('----------分割线----------------')
g1 = (x*2 for x in range(10) if x%2 == 0 )
g2 = tuple(g1)
print(type(g2))
print(g2)


