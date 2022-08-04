##!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import xlrd
import re
import jieba

origin_script = xlrd.open_workbook("HSK4课文文本汇总.xlsx")
sheet_text = origin_script.sheet_by_index(0)
nrows_text = sheet_text.nrows
sheet_new_words = origin_script.sheet_by_index(3)
nrows_word = sheet_new_words.nrows

# 所有的句子合成一个列表
sentence_all = []
for i in range(1, nrows_text):
    text = sheet_text.cell_value(i, 5)
    # print(text)
    text_lesson = sheet_text.cell_value(i, 1)
    text_num = sheet_text.cell_value(i, 2)
    sentence = re.split('[。！；？…… \n]', text)
    # sentence.pop()
    for num in range(len(sentence)):
        text_pair = [text_lesson, text_num, sentence[num]]
        sentence_all.append(text_pair)

# print(sentence_all)

# 查找生词，并且分词里也有这个生词

while True:
    lookup_word = input("请输入要查找的单词：")
    output = []
    for i in range(len(sentence_all)):
        if lookup_word in sentence_all[i][2]:
            output.append(sentence_all[i])
    #print(output)
    if len(output) == 0:
        print("没有找到例句")
    else:
        for sentence in output:
            print("第{}课 课文{}：{}".format(round(sentence[0]), round(sentence[1]), sentence[2]))
    print("========分隔线========")
