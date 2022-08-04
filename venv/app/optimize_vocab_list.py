##!/usr/bin/env python3
# _*_ coding: utf-8 _*_

#读取HSK4文本，把超纲词列出，然后人工校对

import jieba
import xlrd
import xlwt
import re

#jieba.enable_paddle()
jieba.load_userdict('/Users/Arthur/PycharmProjects/CountWords/dict.txt')
punctuation = '/\!:._?,：()《》（）……~“”*""；，。！？、&=>n<\n'
HSK_excel = xlrd.open_workbook('/Users/Arthur/PycharmProjects/CountWords/HSK_HSK_Online_Vocab.xlsx')
HSK_sheet = HSK_excel.sheet_by_index(0)
nrows_HSK = HSK_sheet.nrows

HSK4_excel = xlrd.open_workbook('/Users/Arthur/Documents/GoEast/教学/新HSK资料/词汇/HSK4课文文本汇总.xlsx')
HSK4_text = HSK4_excel.sheet_by_index(0)
nrows_HSK4 = HSK4_text.nrows

HSK4_export_excel = xlwt.Workbook(encoding='utf-8')
HSK4_export_sheet = HSK4_export_excel.add_sheet('sheet1')

def clear_format(text):
    text = str(text)
    text = text.replace('text:',"")
    text = text.replace('\'',"")
    text = text.replace(' ','')
    return text

dict_word_level = {}
for i in range(nrows_HSK):
    word = clear_format(HSK_sheet.cell(i,2))
    level = clear_format(HSK_sheet.cell(i,1))
    dict_word_level[word] = level

#print (text_clear)

extra_word_list = []
for i in range(1, nrows_HSK4):
    text_origin = HSK4_text.cell(i, 4)
    text_clear = clear_format(text_origin)
    word_split = jieba.cut(text_clear, cut_all=False) #HMM=False)
    #dict_count = {"HSK1":0, "HSK2":0, "HSK3":0, "HSK4":0, "HSK5":0, "HSK6":0, "超纲词":0}
    for word in word_split:
        #if word in dict_word_level.keys() and word not in punctuation:
            #dict_count[dict_word_level[word]] = dict_count[dict_word_level[word]]+1
            #print (word, dict_word_level[word])
        if word not in dict_word_level.keys() and word not in punctuation and word not in extra_word_list:
            #dict_count['超纲词'] = dict_count['超纲词'] + 1
            extra_word_list.append(word)

num_write = 0
for item in range(len(extra_word_list)):
    HSK4_export_sheet.write(num_write,0,extra_word_list[item])
    HSK4_export_sheet.write(num_write,1,'超纲词')
    num_write = num_write + 1

HSK4_export_excel.save('./HSK4超纲词统计.xls')

