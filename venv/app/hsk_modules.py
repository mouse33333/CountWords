##!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import xlrd
import re
import jieba

punctuation = '/!:._?,：()《》（）……~“”*""；，。！？、&=><[]【】\\（）+\' '

jieba.set_dictionary("HSK_dict_done.txt")
jieba.load_userdict("user_dict.txt")

eng = []
for i in range(65, 91):
    eng.append(chr(i))
for i1 in range(97, 123):
    eng.append(chr(i1))
for i2 in range(48, 58):
    eng.append(chr(i2))


# 清理读取excel后的格式问题
def clear_format(text):
    text = str(text)
    if 'text' in text:
        text = str(text)
        text = text.replace('text:', '')
        text = text.replace(' ', '')
        text = text.replace('\'', '')
    if 'number' in text:
        text = text.replace('number:', '')
        text = text.replace(' ', '')
        text = text.replace('\'', '')
        text = float(text)
    return text


# 导入excel，返回某一工作表
def import_excel(url, sheet_index):
    excel = xlrd.open_workbook(url)
    sheet = excel.sheet_by_index(sheet_index)
    sheet_rows = sheet.nrows
    return sheet


# 返回HSK词和级别的列表
def word_level(sheet, num):
    dict_word_level = {}
    for i in range(num):
        word = sheet.cell_value(i, 2)
        level = sheet.cell_value(i, 1)
        dict_word_level[word] = level
    return dict_word_level


# 统计一段文本的总字数，不包含标点
def text_characters(text):
    punctuation = ' /!:._?,：()《》（）……~“”*""；，。！？、&=><\n'
    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return len(text)


# 统计一段文本的平均句长
def avg_sentence_len(text):
    length3 = text_characters(text)
    length1 = len(text)
    punctuation = '！，。；？'
    text_without_pnct = re.sub(r'[{}]+'.format(punctuation), '', text)
    length2 = len(text_without_pnct)
    avg_sentence_length = round(length3 / (length1-length2), 2)
    return avg_sentence_length


HSK_sheet = import_excel('HSK2.0_Vocab.xlsx', 0)
sheet_rows = HSK_sheet.nrows
dict_word_level = word_level(HSK_sheet, sheet_rows)


# 清除文本中的数字和英文
def clear_num_eng(text):
    text_split = list(text)
    text_without_num_eng = []
    text_re = ""
    for i3 in text_split:
        if i3 not in eng:
            text_without_num_eng.append(i3)
    for i4 in text_without_num_eng:
        text_re = text_re + i4
    return text_re

# 统计文本的各级别词汇
def text_level(text):
    result = []
    text = clear_num_eng(text.replace("\n", "").replace("\r", ''))
    word_list = list(jieba.cut(text, cut_all=False, HMM=False))
    words_sum = []

    for item in word_list:
        if item in punctuation:
            word_list.remove(item)
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

    rate = [oc_1, oc_2, oc_3, oc_4, oc_5, oc_6, oc_7]
    vocab_num = []
    for item in dict_words.values():
        vocab_num.append(len(item))

    result.append(text_characters(text))  # 总字数
    result.append(len(words_sum))  # 总词数（去重）
    result.append(dict_words)  # 每个级别对应的词
    result.append(vocab_num)  # 每个级别的词数
    result.append(rate)  # 每个级别词数的比例

    return result
