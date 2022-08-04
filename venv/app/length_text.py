##!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import pyperclip
from hsk_modules import text_characters
from hsk_modules import avg_sentence_len

while True:
    #计算一段文本有多少字数，不包括标点符号
    text = input('请复制文本到系统的剪切板，然后按回车进行计算')
    text_origin = pyperclip.paste()
    #print(text_origin)
    text_len = text_characters(text_origin)
    print('文本总字数：', text_len)
    print('===================')

    #计算平均句长
    avg_length = avg_sentence_len(text_origin)
    print('平均句长：', avg_length)
    print('===================')


