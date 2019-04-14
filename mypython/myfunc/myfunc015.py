# -*- coding: utf-8 -*-
'''测试LEGB搜索规则， local --enclosed -- global -- built in  '''

#定义全局变量str --str在内建函数（built in）中是将对象转换为字符串

str = 'global str'

#定义测试的嵌套函数
def outer():
    #定义enclosed层的变量str
    str = 'outer str'

    #定义内层函数
    def inner():
        #定义内存本地变量
        str = 'inner str'
        print(str)

    #调用内层函数
    inner()

#调用外层函数
outer()