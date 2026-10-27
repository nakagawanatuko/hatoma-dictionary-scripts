#!/usr/bin/env python3
# coding: utf-8

# ExtOverlap4Mod.py　OverlapList.txt output1_IPA.txt
# 重複語彙を修正・統合するために抽出。


import sys
import re

Overlap = open(sys.argv[1], "r")

OverlapDic = {}

#   overlapしている項目のIDを辞書化
for line in Overlap:
    line = line.replace('\n','')
    IDs = line.split('\t')
    if IDs[1] != '':
        value = IDs[0]
        key = IDs[1]
        # print(IDs[1])
        if key in OverlapDic:
            OverlapDic[key].append(value)
        else:
            OverlapDic.update({key: [value]})

File = open(sys.argv[2], "r")

Dic = {}

for line in File:
    if line == '\n':
        continue
    item = line.split('\t')
    ID = item[0]
    Dic.update({ID: line})

# print(len(TeXDic))

for key in OverlapDic:
    print(Dic[key], end="")
    for value in OverlapDic[key]:
        print(Dic[value], end="")
