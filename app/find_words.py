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


# 清理格式
def format_clear(text):
    text = str(text)
    text = text.replace('text:', "")
    text = text.replace('\'', "")
    text = text.replace('\\n', '')
    text = text.replace(' ', '')
    text = text.replace('number:', '')
    text = text.replace('.0', '')
    return text


# 所有的句子合成一个列表
sentence_all = []
for i in range(1, nrows_text):
    text = format_clear(sheet_text.cell(i, 4))
    text_lesson = format_clear(sheet_text.cell(i, 1))
    text_num = format_clear(sheet_text.cell(i, 2))
    sentence = re.split('[。！；？……]', text)
    sentence.pop()
    for num in range(len(sentence)):
        text_pair = [text_lesson, text_num, sentence[num]]
        sentence_all.append(text_pair)

# 查找生词，并且分词里也有这个生词
for i in range(1, nrows_word):
    new_word = format_clear(sheet_new_words.cell(i, 0))
    for w in range(len(sentence_all)):
        if new_word in sentence_all[w][2] and new_word in jieba.cut(sentence_all[w][2]):
            print('%s|%s|%s|' % (format_clear(new_word), sentence_all[w][0], sentence_all[w][1]), sentence_all[w][2])
