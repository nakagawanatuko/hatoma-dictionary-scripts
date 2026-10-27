#!/usr/bin/env python3
# coding: utf-8

# ListPron.py output2.txt > output3.txt
# ListPron.py Examples.txt > Examples_IPA.txt
# output2.txt から、[IPA] を取り出し、リスト化する


import sys
import re
import mojimoji

file = open(sys.argv[1], "r")

atta = 0

atta2 = 0

counter = 0

for line in file:
    line = mojimoji.zen_to_han(line, kana=False)
    line = line.replace('i｡','i̥')
    line = line.replace('ï｡','ï̥')
    line = line.replace('u｡','u̥')
    line = line.replace('a｡','ḁ')
    line = line.replace('r｡','r̥')
    line = line.replace('｢','⸢')
    line = line.replace('c,','ç')
    line = line.replace('￢','⸣')
    line = line.replace('{SqBr}','[')
    line = line.replace('{/SqBr}',']')
    line = line.replace('{EOS}','。')
    line = line.replace('。。','。')
    line = line.replace('！。','！')
    line = line.replace('？。','？')
    line = line.replace('’',"'")
    line = line.replace('o＾',"ô")
    line = line.replace('zj','ʒ')
    line = line.replace('jn','ɲ')
    line = line.replace('{\\tone{33}}',"⸠")
    line = line.replace('dʒ','ʤ')
    # i = i.replace('ʤ','dʒ')
    line = line.replace('ts','ʦ')
    line = line.replace('tʃ','ʧ')
    line = line.replace('zj','ʒ')
    line = line.replace('Zj','ʒ')
    line = line.replace('nj','ɲ')
    line = line.replace('dz','ʣ')
    if "{Sec}" in line:
        print(line, end="")
    else:
        for i in line:
            if i == ']':
            # if i == '}':
                atta = 0
            elif i == '[':
            # elif i == '{':
                atta = 1
            if atta == 1:
                i = i.replace('？','?')
                i = i.replace('?','ʔ')
                # i = i.replace('c,','ç')
                i = i.replace('∫','ʃ')
                i = i.replace('N','ŋ')
                i = i.replace('η','ŋ')
                i = i.replace('φ','ɸ')
                i = i.replace('Ф','ɸ')
                i = i.replace('Φ','ɸ')
                i = i.replace('ト','⸠')
                i = i.replace(':','ː')
                # i = i.replace('　', ' ')
            # if i == '}':
            #     atta2 = 0
            # elif i == '{':
            #     atta2 = 1
            # if atta2 == 1:
            #     i = mojimoji.han_to_zen(i, digit=False,ascii=False)
            else:
                i = i.replace('ｳ', 'ゥ')
                i = i.replace('ｲ', 'ィ')
                i = i.replace('ｱ', 'ァ')
                i = i.replace('ｵ', 'ォ')
                i = i.replace('ｴ', 'ェ')
                i = i.replace('ﾜ', 'ヮ')
                i = i.replace('ﾂ', 'ッ')
                i = mojimoji.han_to_zen(i, digit=False,ascii=False)
                i = i.replace(' ','　')
            print(i, end="")

