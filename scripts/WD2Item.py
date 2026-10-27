#!/usr/bin/env python3
# coding: utf-8

# WD2Item.py 20190404_Hatoma.txt > output1.txt
# 加治工先生の鳩間方言辞典をオリジナルのWordファイルから項目、IPA、品詞情報、説明に分ける（タブ区切り）。


import sys
import re

file = open(sys.argv[1], "r")

counter = 0 # Word ID 出力用

counter2 = 0 # Line ID 出力用

# previtem = ''

for line in file:
    counter2 = counter2 + 1
    if re.match("[ァ-ヴ￢｢-]", line):
        counter = counter + 1
        print(counter, end="\t")               # Word ID ではなく行番号が出力されているのであとで修正
        line = line.replace("\n","")
        line = line.replace("[","\t[")
        line = line.replace("]","]\t")
        line = line.replace("）（","/")
        line = line.replace("（","")
        line = line.replace("）","")
        # line2 = line.split('\t')
        # if line2[0] == previtem:
        #     # item = line2[0].replace('￢','')
        #     # item = item.replace('｢','')
        #     print(previtem + '\t' + line2[0])
        # print(line, end='\t')
        # previtem = line2[0]
        print(line, end="\t")
    # elif "{Sec}" in line:
    #     continue
    else:
        line = line.replace("(", "（")
        line = line.replace(")", "）")
        line = re.sub("^　　", "", line)
        line = line.replace("{Exp_", "\t{Exp_")
        if re.search("[①-⑳]", line):
            line = line.replace("①", "{Mn_1}")
            line = line.replace("②", "\t{Mn_2}")
            line = line.replace("③", "\t{Mn_3}")
            line = line.replace("④", "\t{Mn_4}")
            line = line.replace("⑤", "\t{Mn_5}")
            line = line.replace("⑥", "\t{Mn_6}")
            line = line.replace("⑦", "\t{Mn_7}")
            line = line.replace("⑧", "\t{Mn_8}")
            line = line.replace("⑨", "\t{Mn_9}")
            line = line.replace("⑩", "\t{Mn_10}")
            line = line.replace("⑪", "\t{Mn_11}")
            line = line.replace("⑫", "\t{Mn_12}")
            line = line.replace("⑬", "\t{Mn_13}")
            line = line.replace("⑭", "\t{Mn_14}")
            line = line.replace("⑮", "\t{Mn_15}")
            line = line.replace("⑯", "\t{Mn_16}")
            line = line.replace("⑰", "\t{Mn_17}")
            line = line.replace("⑱", "\t{Mn_18}")
            line = line.replace("⑲", "\t{Mn_19}")
            line = line.replace("⑳", "\t{Mn_20}")
        if re.search("（[１-６]）",line):
            line = line.replace("（１）", "{PoS_1}")
            line = line.replace("（２）", "\t{PoS_2}")
            line = line.replace("（３）", "\t{PoS_3}")
            line = line.replace("（４）", "\t{PoS_4}")
            line = line.replace("（５）", "\t{PoS_5}")
            line = line.replace("（６）", "\t{PoS_6}")
            print(line, end="")
        else:
            print(line, end="")





