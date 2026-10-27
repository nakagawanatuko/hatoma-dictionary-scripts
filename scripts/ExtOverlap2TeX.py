#!/usr/bin/env python3
# coding: utf-8

# ExtOverlap2TeX.py OverlapList.txt To_LaTeX2.txt
# 重複した語彙のIDを読み取って、対応するTeXの項目を出力する


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

# print(len(OverlapDic))

# for key in OverlapDic:
#     print(key)
#     for value in OverlapDic[key]:
#         print(value)

File = open(sys.argv[2], "r")

TeXDic = {}

for line in File:
    if line == '\n':
        continue
    item = line.split('{')
    ID = item[1].replace('}','')
    TeXDic.update({ID: line})

# print(len(TeXDic))

for key in OverlapDic:
    print(TeXDic[key])
    for value in OverlapDic[key]:
        print(TeXDic[value])


