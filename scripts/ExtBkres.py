#!/usr/bin/env python3
# coding: utf-8

# ExtBkres.py xxx.txt (方言データの書き起こしファイル)
# 書き起こしの中の（　）に入った相槌を次の行に移す


import sys
import re
import os
# import numpy as np
# import glob

# rootpath='.'

in_file = open(sys.argv[1], "r")

# for root, dirs, files in os.walk(rootpath):
#     for file_ in files:
#         file_path = os.path.join(root,file_).split('/')[-1]
#         files = file_path.split('\n')
#         for i in files:
#             in_file = open(i, "r")
#             for line in i:
#                 print(line)
out_file_name = "out.txt"
out_file = open(out_file_name, 'w')
for line in in_file:
    later = []
    array = re.split('[（）]',line)
    for i in array:
        if re.match('[Ａ-Ｚ][Ａ-Ｚ・]*　', i):
            if '・' in i:
                later2 = []
                later2 = re.split('[・　]', i)
                later3 = later2[0:-1]
                tr = later2[-1]
                for k in later3:
                    j = ''.join(k + '\t' + tr)
                    later.append(j)
            else:
                later.append(i)
        else:
            out_file.write(i.replace('　　','　'))
    for j in later:
        out_file.write(j.replace('　','\t',1) + '\n')
out_file.close()



