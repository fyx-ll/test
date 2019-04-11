# -*- coding: utf-8 -*-
'''输入一个分数，分数在0-100之间，90以上为A，80以上为B，70以上为c,60以上为D，60以下为D，其他数字提示错误'''

#接收输入变量
score = int(input("请输入分数："))

#判断输入的数是否在0-100之间
if score>100 and score<0:
    print("输入的数字有误，请输入0-100之间的数")
else:
    #判断分数所在级别
    if score>=90:
        print("分数是{0}，级别是{1}".format(score,'A'))
    elif score>=80:
        print("分数是{0}，级别是{1}".format(score, 'B'))
    elif score>=70:
        print("分数是{0}，级别是{1}".format(score, 'C'))
    elif score>=60:
        print("分数是{0}，级别是{1}".format(score, 'D'))
    else:
        print("分数是{0}，级别是{1}".format(score, 'E'))
