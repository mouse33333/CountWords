##!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 统计一段文本的词汇在HSK级别的分布情况

import jieba
import pyperclip
from hsk_modules import *
from texttable import Texttable
import pandas as pd

punctuation = '-—★‘’/!:._?,：：()《》（）……~“”*""；，。！？、&=><[]【】\\（）+\' '

HSK_sheet = import_excel('HSK2.0_Vocab.xlsx', 0)
sheet_rows = HSK_sheet.nrows
dict_word_level = word_level(HSK_sheet, sheet_rows)
jieba.set_dictionary("HSK_dict_done.txt")
jieba.load_userdict("user_dict.txt")

while True:
    words_sum = []
    print("=======文本分词分级小程序Beta测试版v0.5=======")
    print("使用说明：以下情况无法正确分词或分级：", "\n"
          "1）多音字：并且分属不同级别，例如长（cháng,chǎng)", '\n'
          "2）切开或合并都存在：例如：要好, 也好, 完了，多发等")
    print('=================================')
    input('请复制文本，不需要粘贴，直接按回车开始统计')
    text_origin = pyperclip.paste().replace("\n", "").replace("\r", '')
    text_no_num_eng = clear_num_eng(text_origin)
    word_list = list(jieba.cut(text_no_num_eng, cut_all=False, HMM=False))
    for item in word_list:
        if item in punctuation:
            word_list.remove(item)
    print("==============分词结果=============")
    print(word_list)
    dict_words = {"HSK1": [], "HSK2": [], "HSK3": [], "HSK4": [],
                  "HSK5": [], "HSK6": [], "超纲词": []}
    for word in word_list:
        if word in dict_word_level.keys() and word not in punctuation and word not in words_sum:
            level = dict_word_level[word]
            for keys in dict_words.keys():
                if level == keys:
                    dict_words[keys].append(word)
            words_sum.append(word)
        elif word not in dict_word_level.keys() and word not in punctuation and word not in words_sum:
            dict_words["超纲词"].append(word)
            words_sum.append(word)

    oc_1 = format((len(dict_words["HSK1"])/len(words_sum)), ".0%")
    oc_2 = format((len(dict_words["HSK2"])/len(words_sum)), ".0%")
    oc_3 = format((len(dict_words["HSK3"])/len(words_sum)), ".0%")
    oc_4 = format((len(dict_words["HSK4"])/len(words_sum)), ".0%")
    oc_5 = format((len(dict_words["HSK5"])/len(words_sum)), ".0%")
    oc_6 = format((len(dict_words["HSK6"])/len(words_sum)), ".0%")
    oc_7 = format((len(dict_words["超纲词"])/len(words_sum)), ".0%")

    oc = []
    for vocab in dict_words.values():
        oc_words = len(vocab)/len(words_sum)
        oc.append(oc_words)
    #print(oc)

    data = [["HSK1", len(dict_words["HSK1"]), oc_1, dict_words["HSK1"]],
            ["HSK2", len(dict_words["HSK2"]), oc_2, dict_words["HSK2"]],
            ["HSK3", len(dict_words["HSK3"]), oc_3, dict_words["HSK3"]],
            ["HSK4", len(dict_words["HSK4"]), oc_4, dict_words["HSK4"]],
            ["HSK5", len(dict_words["HSK5"]), oc_5, dict_words["HSK5"]],
            ["HSK6", len(dict_words["HSK6"]), oc_6, dict_words["HSK6"]],
            ["超纲词", len(dict_words["超纲词"]), oc_7, dict_words["超纲词"]]]
    columns = ["级别", "个数", '占比', '具体词汇']
    df = pd.DataFrame(data=data, columns=columns)
    tb = Texttable()
    tb.set_cols_align(["c", "c", "c", 'l'])
    tb.set_cols_dtype(["t", 'i', 'i', 't'])
    tb.set_cols_width([8, 8, 8, 40])
    tb.header(df.columns)
    tb.add_rows(df.values, header=False)

    print('========根据HSK2.0词汇表统计信息========')
    print('1）总字数', text_characters(text_no_num_eng))
    print('2）平均句长', avg_sentence_len(text_origin), "个字")
    print("3）词汇分析：\n", tb.draw())

# 多义词：多发；要好；也好，一字多义，才能，好人（经济条件越好人就越幸福），算是，没什么，话说，多年，买好，（填写）完了
# 一字原则：加一字，少一字都可，少一字不成词的，酌情考虑，多余的都算超纲；其他语义的也算超纲
# 需要==>需；选择==>选
# 检查==>查
