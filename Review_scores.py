# -*- coding: utf-8 -*-
"""
程序名称：长鸡蛋统计小帮手
题目要求：
读入CSV文件
列出总和、平均分以及等级（甲、乙、丙、丁）
甲：平均80~100分
乙：平均60~79分
丙：平均50~59分
丁：平均50分以下
"""
import csv

print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % ("", "姓名", "总分", "平均分", "等级"))

with open("scores.csv", encoding="gbk") as csvfile:
    x = 0
    for row in csv.reader(csvfile):
        if x > 0:
            score_total = int(row[1]) + int(row[2]) + int(row[3])
            average = round(score_total / 3, 1)
            if average >= 80:
                grade = "甲"
            elif 60 <= average < 80:
                grade = "乙"
            elif 50 <= average < 60:
                grade = "丙"
            else:
                grade = "丁"
            print("%d\t\t%s\t\t%d\t\t%d\t\t%s" % (x, row[0], score_total, average, grade))
        x += 1
