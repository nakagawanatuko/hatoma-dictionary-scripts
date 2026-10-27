#!/usr/bin/env python3
# coding: utf-8

# To_LaTeX.py To_LaTeX1.txt
# To_LaTeX1.txt から、TeX用のフォーマットを生成

# To_LaTeX.py To_LaTeX1.txt > To_LaTeX2.txt
# 修正用に項目すべてを1ファイルに出力している。

import sys
import re

file = open(sys.argv[1], "r")

counter = 1

# ファイル生成時はここのコメントアウトを外す
file_name = "./{}.tex".format(counter)
out_file = open(file_name, 'w')
out_file.write('''
% !TEX root = ../main.tex

\chapter*{ア}
\\addcontentsline{toc}{chapter}{ア}
\\addthumb{1}{}{white}{gray}

\\begin{multicols}{2}

''')
# ここまで

for line in file:
    line = line.replace('。\n', '')
    line = line.replace('\n', '')
    line = line.replace('⸣', '{\cnr}')
    line = line.replace('⸢', '{\opcnr}')
    line = line.replace('[', '\ipa{[')
    line = line.replace(']', ']}')
    line = line.replace('⸠', '{$\\assert$}')
    line = line.replace('□', '{$\square$}')
    line = line.replace('△', '{$\\triangle$}')
    line = line.replace('○', '{$\\bigcirc$}')
    line = line.replace('{Ref_', '{')
    line = line.replace('{Mn_', '\Mn{')
    line = line.replace('{PoS_', '\PoS{')
    line = line.replace('{Sg_', '\PoS{')
    line = line.replace('{Exp_', '\PoS{')
    line = line.replace('{Rel_', '\PoS{')
#     line = line.replace('　', ' ')
    line = line.replace('→', '$\\to$')
    line = line.replace('~', '〜')
    line = line.replace('\\ruby\\ipa{[g]}', '\\ruby[g]')
#     line = re.sub('\\kaeriten\{[一二㆑]\}','',line)
    line = line.replace('\kaeriten\{','{')
    line = line.replace('ǒ', '\\v{o}')
    line = line.replace('ũ', '\~{u}')
    line = line.replace('ã', '\~{a}')
    line = line.replace('{Break}', '')
    line = line.replace('{EOS}', '。')
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
        # continue
# ファイル生成時はここのコメントアウトを外す
        out_file.write('''
\end{multicols}
        ''')
        out_file.close()
        counter = counter + 1
        file_name = "./{}.tex".format(counter)
        out_file = open(file_name, 'w')
        title = line.replace("\n", "")
        title = title.replace("{Sec}", "")
        title = title.replace("{/Sec}", "")
        out_file.write('''
%% !TEX root = ../main.tex

\chapter*{%s}
\\addcontentsline{toc}{chapter}{%s}
\\addthumb{%d}{}{white}{gray}
\\begin{multicols}{2}

        '''%(title,title,counter))
# ここまで
    else:
        items = line.split('\t')
        WdID = items[0]
        Wd = items[1]
        WdIPA = items[2]
        PoS = items[3]
        Desc = ''.join(items[4:])
        if "/" not in PoS:
                out_file.write("\entry{" + Wd + "}{" + WdIPA + "}{}{" + PoS + "}{" + Desc + "。}\n\n")
        else:
                # out_file.write("Multiple PoS here!!!\n\n")
                PoSs = PoS.split('/')
                Descs = re.split('\\\PoS\{[1-9]\}',Desc)
                ctr = 0
                for i in PoSs:
                        # print(Descs[0])
                        if ctr == 0:
                                out_file.write("\entry{" + Wd + "}{" + WdIPA + "}{\PoS{" + str(ctr+1) + "}}{" + PoSs[ctr] + "}{" + Descs[ctr+1] + "}\n")
                        elif ctr +1 == len(PoSs):
                                out_file.write("\entrym{" + "\PoS{" + str(ctr+1) + "}}{" + PoSs[ctr] + "}{" + Descs[ctr+1] + "。}\n")
                        else:
                                out_file.write("\entrym{" + "\PoS{" + str(ctr+1) + "}}{" + PoSs[ctr] + "}{" + Descs[ctr+1] + "}\n")
                        ctr = ctr + 1
                out_file.write("\n\n")
# ファイル生成時はここのコメントアウトを外す
        # out_file.write("\entry{" + WdID  + "}{" + Wd + "}{" + WdIPA + "}{" + PoS + "}{" + Desc + "。}\n\n")
# ここまで
        # print("\entry{" + WdID  + "}{" + Wd + "}{" + WdIPA + "}{" + PoS + "}{" + Desc + "。}\n")


# ファイル生成時はここのコメントアウトを外す
out_file.write('''\end{multicols}''')

out_file.close()
# ここまで