#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

#统计一本教材：每课文本长度；平均文本字数；平均文本长度；
#excel模板格式：
#sheet1：全文本：教材；课编号；课文编号；角色；文本
#sheet2：对话文本：教材；课编号；课文编号；角色；文本
#sheet3：叙述文本：教材；课编号；课文编号；角色；文本


import xlrd
import re
import string
import jieba
import zhon.hanzi
punctuation = string.punctuation + zhon.hanzi.punctuation

origin_script = xlrd.open_workbook("/users/Arthur/Documents/GoEast/教学/新HSK资料/词汇/HSK4课文文本汇总.xlsx")
sheet_1 = origin_script.sheet_by_index(2)
nrows = sheet_1.nrows

def delete_head(text):
    text = str(text)
    text = text.replace('\\n','')
    text = text.replace('\'','')
    text = text.replace('text:','')
    text = text.replace(' ','')
    return text

def remove_punctuation(text):
    new_text = re.sub(r'[{}]+'.format(punctuation),'',text)
    return new_text

text_length = []
text_length_sum = 0

for i in range(1,nrows):
    text_origin = sheet_1.cell(i,4)
    text_no_head_no_pun = remove_punctuation(delete_head(text_origin))
    text_length.append(len(text_no_head_no_pun))

for i in range(len(text_length)):
    text_length_sum = text_length_sum + text_length[i]

print ("每课文本长度:", text_length)
print ("文本数量:", len(text_length))
print ("文本总字数：",text_length_sum)
print ("平均文本长度：", text_length_sum/len(text_length))
