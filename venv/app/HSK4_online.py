##!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 统计词汇总数
# 以及各个级别的HSK词汇数量
# 并且输出某一级别以上（包括超纲词）的词汇

import jieba
import pyperclip
from hsk_modules import *

punctuation = '/!:._?,：()《》（）[]……~“”*""；，。！？、&=<>\n1234567890'

HSK_sheet = import_excel('/Users/Arthur/PycharmProjects/CountWords/HSK_HSK_Online_Vocab.xlsx', 0)
sheet_rows = HSK_sheet.nrows
dict_word_level = word_level(HSK_sheet, sheet_rows)

while True:
    words_sum = []
    print("==========================")
    input('请复制文本，并按回车开始统计\n')
    print('==========================')
    text_origin = pyperclip.paste()
    word_split = jieba.cut(text_origin, cut_all=False)
    hsk1 = []
    hsk2 = []
    hsk3 = []
    hsk4 = []
    hsk5 = []
    hsk6 = []
    extra = []
    for word in word_split:
        if word in dict_word_level.keys() and word not in punctuation and word not in words_sum:
            words_sum.append(word)
            if dict_word_level[word] == "HSK1":
                hsk1.append(word)
            if dict_word_level[word] == "HSK2":
                hsk2.append(word)
            if dict_word_level[word] == "HSK3":
                hsk3.append(word)
            if dict_word_level[word] == "HSK4":
                hsk4.append(word)
            if dict_word_level[word] == "HSK5":
                hsk5.append(word)
            if dict_word_level[word] == "HSK6":
                hsk6.append(word)
        elif word not in dict_word_level.keys() and word not in punctuation and word not in words_sum:
            words_sum.append(word)
            extra.append(word)

    print('=========统计信息=========')
    print('总字数', text_characters(text_origin))
    print("HSK1：", len(hsk1), '\n'
          "HSK2：", len(hsk2), '\n'
          "HSK3：", len(hsk3), '\n'
          "HSK4：", len(hsk4), '\n'
          "HSK5：", len(hsk5), '\n'
          "HSK6：", len(hsk6), '\n'
          "超纲词：", len(extra))

    print('========生词========')
    print('========HSK4========')
    for item in hsk4:
        print(item)
    print('========HSK5========')
    for item in hsk5:
        print(item)
    print('========HSK6========')
    for item in hsk6:
        print(item)
    print('========超纲词========')
    for item in extra:
        print(item)
