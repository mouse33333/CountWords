##!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 批量输出
# 文本的总字数，总词数（去重），分词结果，每个级别的词汇，每个级别的词汇个数，每个级别的词汇占比

from hsk_modules import *
import xlrd
import xlwt

excel = xlrd.open_workbook('/Users/Arthur/PycharmProjects/CountWords/HSK4课文文本汇总.xlsx')
sheet = excel.sheet_by_index(0)
rows = sheet.nrows

new_excel = xlwt.Workbook()
new_sheet = new_excel.add_sheet("sheet1")


for num in range(1, rows):
    text = sheet.cell_value(num, 4)
    count_num = 0
    for item in text_level(text):
        print(type(item))
        if isinstance(item, int):
            new_sheet.write(num, count_num, item)
            count_num = count_num + 1
        if isinstance(item, dict):
            new_sheet.write(num, count_num, str(item))
            count_num = count_num + 1
        if isinstance(item, list):
            for i in range(len(item)):
                new_sheet.write(num, count_num, item[i])
                count_num = count_num + 1

new_excel.save('/Users/Arthur/PycharmProjects/test.xls')
