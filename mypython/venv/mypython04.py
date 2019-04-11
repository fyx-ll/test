# -*- coding: utf-8 -*-
row1= {"name": "a1","age": 18, "salary":30000,"city":"beijing"}
row2= {"name": "a2","age": 19, "salary":20000,"city":"shanghai"}
row3= {"name": "a3","age": 20, "salary":10000,"city":"shengzheng"}

tb = [row1,row2,row3]

#获得第二行的人薪资
print('第二行人的薪资是:{0}'.format(tb[1].get("salary")))

#打印表中所有的薪资
for i in range(3):
    print('{0}的薪资是:{1}'.format(tb[i].get('name'),tb[i].get("salary")))

#打印表的所有数据。
for i in range(3):
    print('{0}的年龄是：{1}，薪资是：{2}，所在城市是：{3}'.format(tb[i].get('name'), tb[i].get('age'), tb[i].get('salary'), tb[i].get('city')))
