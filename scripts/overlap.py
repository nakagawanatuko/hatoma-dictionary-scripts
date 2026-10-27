#!/usr/bin/env python3
# coding: utf-8

# overlap.py output4.txt > overlap.py
# 重複語彙検出


import sys
import re

file = open(sys.argv[1], "r")

counter = 0
atta = 0

previ = ''
nexti = ''
items2 = []
lines = []

for line in file:
    if "{Sec}" in line:
        continue
    else:
        items = line.split('\t')
        items2.append(items[1])
        lines.append(line)

for i in items2:
    nexti = items2[counter+1]
    if i == nexti:
        print(lines[counter], end='')
    elif i == previ:
        print(lines[counter], end='')
    previ = i
    counter = counter + 1


