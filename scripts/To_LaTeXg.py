#!/usr/bin/env python3
# coding: utf-8

# To_LaTeX2.py output_g_1.txt
# output_g_1.txt から、TeX用のフォーマットを生成

import sys
import re

file = open(sys.argv[1], "r")

counter = 1

# ファイル生成時はここのコメントアウトを外す
# file_name = "./{}.tex".format(counter)
# out_file = open(file_name, 'w')
# out_file.write('''
# % !TEX root = ../main.tex

# \chapter*{ア}
# \\addcontentsline{toc}{chapter}{ア}
# \\addthumb{1}{}{white}{gray}

# \\begin{multicols}{2}

# ''')
# ここまで

for line in file:
    line = line.replace('⸣', '{\cnr}')
    line = line.replace('⸢', '{\opcnr}')
    line = line.replace('[', '\ipa{[')
    line = line.replace(']', ']}')
    line = line.replace('⸠', '{\\tone{33}}')
    line = line.replace('□', '{$\square$}')
    line = line.replace('△', '{$\\triangle$}')
    line = line.replace('○', '{$\bigcirc$}')
    line = line.replace('　', ' ')
    line = line.replace('／', '/')
    line = line.replace('→', '$\\to$')
    line = line.replace('\\ruby\\ipa{[g]}', '\\ruby[g]')
    line = line.replace("①", "\Mn{1}")
    line = line.replace("②", "\Mn{2}")
    line = line.replace("③", "\Mn{3}")
    line = line.replace("④", "\Mn{4}")
    line = line.replace("⑤", "\Mn{5}")
    line = line.replace("⑥", "\Mn{6}")
    line = line.replace("⑦", "\Mn{7}")
    line = line.replace("⑧", "\Mn{8}")
    line = line.replace("⑨", "\Mn{9}")
    line = line.replace("⑩", "\Mn{10}")
    line = line.replace("⑪", "\Mn{11}")
    line = line.replace("⑫", "\Mn{12}")
    line = line.replace("⑬", "\Mn{13}")
    line = line.replace("⑭", "\Mn{14}")
    line = line.replace("⑮", "\Mn{15}")
    line = line.replace("⑯", "\Mn{16}")
    line = line.replace("⑰", "\Mn{17}")
    line = line.replace("⑱", "\Mn{18}")
    line = line.replace("⑲", "\Mn{19}")
    line = line.replace("⑳", "\Mn{20}")
    line = line.replace("㉑", "\Mn{20}")
    line = line.replace("㉒", "\Mn{20}")
    line = line.replace("㉓", "\Mn{20}")
    # line = re.sub('（[０-９]+）', '[item]', line)
#   以下はXeLaTeXのときにはコメントアウトする
    # line = line.replace('ʔ', 'p')
    # line = line.replace('ʒ', 'Z')
    # line = line.replace('ʃ', '')
    # line = line.replace('ç', '\c{c}')
    # line = line.replace('ŋ', 'N')
    # line = line.replace('Φ', 'F')
    # line = line.replace('ː', ':')
    # line = line.replace('i̥', '\\r*i')
    # line = line.replace('ï̥', '\\r*{\\"{i}}')
    # line = line.replace('u̥', '\\r*u')
    # line = line.replace('ḁ', '\\r*a')
    # line = line.replace('r̥', '\\r*r')
    # line = line.replace('⸠', '???')
#   ここまでXeLaTeXのときはコメントアウト
    if "{Sec}" in line:
        continue
    print(line, end="")
# ファイル生成時はここのコメントアウトを外す
#         out_file.write('''
# \end{multicols}
#         ''')
#         out_file.close()
#         counter = counter + 1
#         file_name = "./{}.tex".format(counter)
#         out_file = open(file_name, 'w')
#         title = line.replace("\n", "")
#         title = title.replace("{Sec}", "")
#         title = title.replace("{/Sec}", "")
#         out_file.write('''
# %% !TEX root = ../main.tex

# \chapter*{%s}
# \\addcontentsline{toc}{chapter}{%s}
# \\addthumb{%d}{}{white}{gray}
# \\begin{multicols}{2}

#         '''%(title,title,counter))
# ここまで
#     else:
#         items = line.split('\t')
#         WdID = items[0]
#         Wd = items[1]
#         WdIPA = items[2]
#         PoS = items[3]
#         Desc = ''.join(items[4:])
# # ファイル生成時はここのコメントアウトを外す
#         # out_file.write("\entry{" + WdID  + "}{" + Wd + "}{" + WdIPA + "}{" + PoS + "}{" + Desc + "。}\n\n")
# # ここまで
#         print("\entry{" + WdID  + "}{" + Wd + "}{" + WdIPA + "}{" + PoS + "}{" + Desc + "。}\n")


# ファイル生成時はここのコメントアウトを外す
# out_file.write('''\end{multicols}''')

# out_file.close()
# ここまで