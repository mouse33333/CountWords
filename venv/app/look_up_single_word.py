##!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 在HSK2.0, 3.0以及blended课程中查找单词

import xlrd
import prettytable as pt
from textwrap import fill

origin_script_hsk2 = xlrd.open_workbook("HSK2.0_vocab.xlsx")
HSK2_vocab = origin_script_hsk2.sheet_by_index(0)
nrows_HSK2 = HSK2_vocab.nrows

origin_script_hskb = xlrd.open_workbook("HSK Blended_vocab.xlsx")
HSK_blended_vocab = origin_script_hskb.sheet_by_index(0)
nrows_HSK_blended = HSK_blended_vocab.nrows

origin_script_hsk3 = xlrd.open_workbook("HSK3.0_vocab.xlsx")
HSK3_vocab = origin_script_hsk3.sheet_by_index(0)
nrows_HSK3 = HSK3_vocab.nrows

origin_script_hsk4 = xlrd.open_workbook('HSK4课文文本汇总.xlsx')
HSK4_text = origin_script_hsk4.sheet_by_index(0)
nrows_HSK4 = HSK4_text.nrows

print("本词汇库包含\n【HSK2.0考纲生词】共{s1}个\n"
      "【HSK3.0考纲L1~L6级生词】共{s3}个\n"
      "【HSK Blended生词】共{s2}个\n"
      .format(s1=nrows_HSK2-1, s2=nrows_HSK_blended-1, s3=nrows_HSK3-1))

def format_clear(text):
    text = str(text)
    text = text.replace('text:', "")
    text = text.replace('\'', "")
    text = text.replace('\\n', '')
    text = text.replace(' ', '')
    text = text.replace('number:', '')
    text = text.replace('.0', '')
    return text


look_up_word = 1

while True:
    look_up_word = input("请输入要查询的词，并按回车：（结束查询按q+回车）\n")
    if look_up_word == 'q':
        break
    else:
        count_1 = 0
        tb = pt.PrettyTable()
        tb.field_names = ["HSK版本", "词汇", "拼音", "翻译", "级别"]
        tb.align["拼音"] = "l"
        tb.align["翻译"] = "l"
        for i in range(nrows_HSK2):
            cell_level = HSK2_vocab.cell_value(i, 1)
            cell_word = HSK2_vocab.cell_value(i, 2)
            cell_pinyin = HSK2_vocab.cell_value(i, 3)
            cell_translation = HSK2_vocab.cell_value(i, 4)
            if look_up_word == cell_word:
                #print('HSK2.0查询结果：', look_up_word, cell_pinyin, cell_translation, cell_level)
                tb.add_row(["HSK2.0", look_up_word, cell_pinyin, fill(cell_translation, width=30), cell_level])
            else:
                count_1 = count_1 + 1
            if count_1 == nrows_HSK2:
                print(look_up_word + "：", "不是HSK2.0词汇")

        count_3 = 0
        for i in range(nrows_HSK3):
            cell_word = HSK3_vocab.cell_value(i, 0)
            cell_pinyin = HSK3_vocab.cell_value(i, 1)
            cell_translation = HSK3_vocab.cell_value(i, 2)
            cell_level = HSK3_vocab.cell_value(i, 7)
            if look_up_word == cell_word:
                #print('HSK3.0查询结果：', look_up_word, cell_pinyin, cell_translation, cell_level)
                tb.add_row(["HSK3.0", look_up_word, cell_pinyin, fill(cell_translation, width=30), cell_level])
            else:
                count_3 = count_3 + 1
            if count_1 == nrows_HSK3:
                print(look_up_word + "：", "不是HSK3.0词汇")

        count_2 = 0
        for i in range(1, nrows_HSK_blended):
            list_blended = []
            cell_word = HSK_blended_vocab.cell_value(i, 3)
            cell_pinyin = HSK_blended_vocab.cell_value(i, 4)
            cell_translation = HSK_blended_vocab.cell_value(i, 5)
            cell_word_lesson = int(HSK_blended_vocab.cell_value(i, 2))
            cell_word_level = HSK_blended_vocab.cell_value(i, 1)
            cell_level = '{s1}-Blended第{s2}课'.format(s1=cell_word_level, s2=cell_word_lesson)
            if look_up_word == cell_word:
                #print('HSK Blended查询结果：', look_up_word, cell_pinyin, cell_translation, cell_level)
                tb.add_row(["HSK Blended", look_up_word, cell_pinyin, fill(cell_translation, width=30), cell_level])
            else:
                count_2 = count_2 + 1
            if count_2 == nrows_HSK_blended:
                print(look_up_word + "：", "不是HSK Blended词汇")
    print(tb)
    print("==========分割线==========")
