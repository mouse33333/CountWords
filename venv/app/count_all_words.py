#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 统计输出：每篇文本的词数；文本总数量；文本总词数；平均每篇文本的词数

import xlrd
import re
import string
import jieba
import zhon.hanzi
punctuation = string.punctuation + zhon.hanzi.punctuation

print (punctuation)

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

words_num = []

for i in range(1,nrows):
    seg_list = []
    text_origin = sheet_1.cell(i,4)
    text_no_head = delete_head(text_origin)
    text_no_head_no_pun = remove_punctuation(text_no_head)
    seg_list = list(jieba.cut(text_no_head_no_pun))
    words_num.append(len(seg_list))

words_sum = 0
for i in range(len(words_num)):
    words_sum = words_sum + words_num[i]

print ("每篇文本的词数:",words_num)
print ("文本总数量:", len(words_num))
print ("文本总词数:",words_sum)
print ("平均每篇文本的词数:",words_sum/len(words_num))
