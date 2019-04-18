# -*- coding: utf-8 -*-
'''测试析构函数'''

class Person:
    def __del__(self): #重新__del__方法
        print('销毁对象：{0}'.format(self))

p1 = Person()
p2 = Person()
print('p1:', p1)
print('p2:', p2)
del p2  #调用del函数删除实例对象p2
print('程序结束')

#程序结束后垃圾回收机制回调用该对象的__del__方法删除对象