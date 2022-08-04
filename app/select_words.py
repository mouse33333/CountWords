##!/usr/bin/env python3
# _*_ coding: utf-8 _*_

with open('/Users/Arthur/Documents/GoEast/教学/新HSK资料/HSK常用词例句_fromBCC.txt', 'rt') as hsk_words:
    text_lines = hsk_words.readlines()

words = []
for line in text_lines:
    if '#' in line:
        line = line.replace('#', '')
        #line = line.replace('\n', '')
        words.append(line)

with open('/Users/Arthur/Documents/GoEast/教学/新HSK资料/words_bbc.txt', 'wt') as out_file:
    for out_line in words:
        out_file.writelines(out_line)

print(len(words))
