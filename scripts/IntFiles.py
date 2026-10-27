#!/usr/bin/env python3
# coding: utf-8

# IntFiles.py OverlapList_corrected.txt 20191226作業.txt 20191016_Hatoma.txt
# 削除された項目は消す

import sys
import re

OList = open(sys.argv[1], "r")
O = open(sys.argv[2], "r")
Main = open(sys.argv[3], "r")

olist = []
ODict = {}
Erase = []
MDict = {}

for line in O:
    line = line.replace('\n', '')
    line = line.split('\t')
    ID = line[0]
    ODict[ID] = line[1:]
    olist.append(ID)

for line in OList:
    oID = line.replace('\n', '')
    if oID not in olist:
        Erase.append(oID)

for line in Main:
    line = line.replace('\n', '')
    line = line.split('\t')
    MID = line[0]
    MContent = line[1:]
    MDict[MID] = MContent
    if MID in olist:
        MDict[MID] = ODict[MID]
    elif MID in Erase:
        MDict[MID] = ''

for i in MDict:
    if MDict[i] == '':
        continue
    print(i, end="")
    for k in MDict[i]:
        print('\t', end='')
        print(k, end='')
    print('\n', end='')


