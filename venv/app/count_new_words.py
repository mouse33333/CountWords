#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

for num in range(1,21):
    url = "/users/Arthur/desktop/Text/Lesson%s.txt" %num
    file_read = open(url,'r')
    try:
        all_the_text = file_read.read()
    finally:
        file_read.close()

    import re
    punctuation = '/！:。，._？,：、《》（）……~“”*'
    def remove_punctuation(text):
        new_text = re.sub(r'[{}]+'.format(punctuation),'',text)
        return new_text

    no_punctuation = remove_punctuation(all_the_text)

    import jieba
    seg_list = jieba.cut(no_punctuation)
    new_seg_list = []
    for i in seg_list:
        if i not in new_seg_list:
            new_seg_list.append(i)

    word_list = '\n'.join(new_seg_list)

    file_write= open("/users/Arthur/desktop/WordList/Lesson%s-wordlist.txt" %num,'w')
    file_write.write(word_list)
    file_write.close()
    print(url)
    num = num + 1
