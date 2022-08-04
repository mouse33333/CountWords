#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import xlrd

x1 = xlrd.open_workbook('/users/Arthur/Desktop/课消明细表.xls')

sheet1 = x1.sheet_by_index(0)
sheet2 = x1.sheet_by_index(1)

nrows1 = sheet1.nrows
nrows2 = sheet2.nrows

print (nrows1,nrows2)

def clear_format(text):
    text = str(text)
    if 'number' in text:
        text = text.replace('\\n','')
        text = text.replace('\'','')
        text = text.replace('number:','')
        #text = text.replace(' ','')
        return float(text)
    if 'text' in text:
        text = text.replace('\\n','')
        text = text.replace('\'','')
        text = text.replace('text:','')
        #text = text.replace(' ','')
        return text

for n2 in range(nrows2):
    learning_hour = 0
    v1 = str(sheet2.cell(n2,0))
    list_date = []
    for n1 in range(nrows1):
        v_lookup = str(sheet1.cell(n1,0))
        if v_lookup == v1:
            learning_hour = learning_hour + clear_format(sheet1.cell(n1,15))
            v_teacher = clear_format(sheet1.cell(n1,5))
            list_date.append(clear_format(sheet1.cell(n1,12)))
    print (clear_format(v1), ";",v_teacher, ";",learning_hour, ";", min(list_date))

