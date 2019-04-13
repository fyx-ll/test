# -*- coding: utf-8 -*-
'''测试lambda表达式和匿名函数'''

f = lambda a, b, c: a+b+c

print(f)
print(type(f))
print(f(1, 2, 3))

g = [lambda a: a*2, lambda b: b*3, lambda c: c*4]
print(g)
print(type(g))
print(g[0](2), g[1](3), g[2](4))

t = (lambda a: a*2, lambda b: b*3, lambda c: c*4)
print(t)
print(type(t))
print(t[0](2), t[1](3), t[2](4))

