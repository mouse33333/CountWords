#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 统计HSK4文本的平均句长，平均字数

import xlrd
import re
import string
punctuation = '，。；？！'

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

def cal_sentence_length(text):
    text_no_head = delete_head(text)
    len_a = len(text_no_head)
    text_no_pun = remove_punctuation(text_no_head)
    len_b = len(text_no_pun)
    sentence_length = round(len_b / (len_a-len_b),1)
    return sentence_length

sentence_length_list = []
sentence_length_sum = 0
for i in range(1,nrows):
    origin_text = sheet_1.cell(i,4)
    sentence_length_list.append(cal_sentence_length(origin_text))

for i in range(len(sentence_length_list)):
    sentence_length_sum = sentence_length_sum + sentence_length_list[i]

print ("每篇文本平均句长：",sentence_length_list)
print ("文本总数:",len(sentence_length_list))
print ("句子长度总数:", sentence_length_sum)
print ("平均句长:", sentence_length_sum/len(sentence_length_list))
