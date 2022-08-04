#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

#统计在HSK4文本里的词汇的出现次数

import xlrd
import re
import string
import zhon.hanzi
import jieba
punctuation = string.punctuation + zhon.hanzi.punctuation

origin_script = xlrd.open_workbook("/users/Arthur/Documents/GoEast/教学/新HSK资料/词汇/HSK4课文文本汇总.xlsx")
sheet_1 = origin_script.sheet_by_index(0)
sheet_2 = origin_script.sheet_by_index(3)
nrows_text = sheet_1.nrows
nrows_words = sheet_2.nrows

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

dict_word_num = {}

def get_all_text(num):
    text_all = []
    for i in range(1, num):
        text_origin = sheet_1.cell(i,4)
        text_no_head_no_pun = remove_punctuation(delete_head(text_origin))
        text_words_list = list(jieba.cut(text_no_head_no_pun))
        text_all = text_all + text_words_list
    return text_all

text_all = get_all_text(nrows_text)

for i in range(1,nrows_words):
    new_word = sheet_2.cell(i,0)
    new_word_no_head = delete_head(new_word)
    count = 0
    for i in range(len(text_all)):
        if new_word_no_head == text_all[i]:
            count = count + 1
    dict_word_num[new_word_no_head] = count

new_dict = sorted(dict_word_num.items(), key=lambda x:x[1], reverse=True)

for i in new_dict:
    print(i)



