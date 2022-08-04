##!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import xlrd
from hsk_modules import clear_format


# from clear_format import clear_format


def import_excel(url, sheet_index):
    excel = xlrd.open_workbook(url)
    sheet = excel.sheet_by_index(sheet_index)
    sheet_rows = sheet.nrows
    return sheet


def word_level(sheet, num):
    dict_word_level = {}
    for i in range(num):
        word = clear_format(sheet.cell(i, 2))
        level = clear_format(sheet.cell(i, 1))
        dict_word_level[word] = level
    return dict_word_level

# sheet = import_excel('/Users/Arthur/PycharmProjects/CountWords/HSK_HSK_Online_Vocab.xlsx',0)
# print (type(clear_format(sheet.cell(0,0))))
