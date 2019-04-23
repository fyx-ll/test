# -*- coding: utf-8 -*-

class Person:

    def work(self):
        print("努力上班！")


def play_game(s):
    print('{0}在玩游戏'.format(s))

def work2(s): #注意重写方法必须和被重写方法的形参一致。
    print('好好学习，天天向上！')

def work3():
    print('work3')

Person.play = play_game

p = Person()
print(Person) #Person 在内存中的地址
print(p)      #p在内存中的地址
p.play() #解释器实际调用的流程是 Person.play(p) ,将 p 值传给play

print('重写work方法前的打印', p.work())
Person.work = work2  #重写work方法
print('重写work方法后的打印', p.work())
