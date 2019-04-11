# -*- coding: utf-8 -*-
'''输入一个学生的成绩，将其转化成简单的描述：不及格（小于60），及格（60-79），良好（80-89），
优秀（90-100）'''

#接受传入的分数变量
score = int(input("请输入分数："))

#接受要打印的描述
grade = ''

#方法一（使用完整的条件表达式）
if score < 60:
    grade = '不及格'
if 60<= score <80:
    grade = '及格'
if 80< score <90:
    grade = '良好'
if 90 < score :
    grade = '优秀'
print("分数{0}是{1}".format(score, grade))
print('******************分割线****************')
#方法二（使用多分支结构）
if score < 60:
    grade = '不及格'
elif score <80:
    grade = '及格'
elif score <90:
    grade = '良好'
else :
    grade = '优秀'

print("分数{0}是{1}".format(score, grade))
