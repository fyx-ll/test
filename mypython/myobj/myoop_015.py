# -*- coding: utf-8 -*-
'''测试多重继承和mro()'''

class A:
    def aa(self):
        print('aa')

class B:
    def bb(self):
        print('bb')

class C(A, B):
    def cc(self):
        print('cc')

print(C.mro())
c1 = C()
#C 继承了 A 和 B
c1.aa()
c1.bb()
c1.cc()