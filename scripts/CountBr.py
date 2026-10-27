#!/usr/bin/env python3
# coding: utf-8

# CountBr.py 20190404_Hatoma.txt
# 加治工先生の鳩間方言辞典をオリジナルのWordファイルからカッコ矛盾の行数（と始まり括弧と終わり括弧の数）を表示。


import sys
import re

file = open(sys.argv[1], "r")

counter = 0

lines = []

for line in file:
    counter = counter + 1
    LeftBr = line.count('{')
    RightBr = line.count('}')
    if LeftBr > RightBr:
        print(str(LeftBr) + "\t" + str(RightBr) + "\t" + str(counter))
    elif RightBr < LeftBr:
        print(str(LeftBr) + "\t" + str(RightBr) + "\t" + str(counter))




