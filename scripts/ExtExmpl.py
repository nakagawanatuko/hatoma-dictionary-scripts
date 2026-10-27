#!/usr/bin/env python3
# coding: utf-8

# ExtExmpl.py output1.txt > output2.txt
# output1.txt から、例文、IPA、訳を抜き出す。


import sys
import re

file = open(sys.argv[1], "r")

file_name = "./Examples.txt"
out_file = open(file_name, 'w')
out_file.write("WdID" + "\t" + "Wd" + "\t" + "SID" + "\t" + "Ex" + "\t" + "IPA" + "\t" + "Trs" + "\n")

SID = 1

print("WdID" + "\t" + "PoSID" + "\t" + "MnID" + "\t" + "SID" + "\t" + "Wd" + "\t" + "WdIPA" + "\t" + "PoS" + "\t" + "Description")

counter = 1

counter2 = 0

for line in file:
    counter2 = counter2 + 1
    if counter2 == 1:
        continue
    elif "{Sec}" in line:
        continue
    line = line.replace("。\n", "")
    items = line.split("\t")
    ID = str(counter)
    WdID = items[0]
    OvlpID = items[1]
    if OvlpID != "":
        Wd = ""
        WdIPA = ""
        PoS = ""
        Desc = ""
    else:
        Wd = items[3]
        WdIPA = items[4]
        PoS = items[5]
        Desc = items[6:]
    Examples = []
    PoSList = []
    # print(ID + '\t' + WdID + '\t' + OvlpID + '\t' + Wd + '\t' + WdIPA + '\t' + PoS)
    for i in Desc:
        counter = counter + 1
        i = i.replace("\n","")
        if "{Mn_" in i:
            Match = re.search("{Mn_[0-9]+", i)
            MatchedMn = Match.group(0)
            MnID = MatchedMn[4:]
        else:
            MnID = str(0)
        if int(MnID) > 1 and int(PoSID) > 0:
            PoSID = PoSID
        elif "{PoS_" in i:
            Match = re.search("{PoS_[0-9]+", i)
            MatchedPoS = Match.group(0)
            PoSID = MatchedPoS[5:]
        # elif "{Exp_" in i:
        #     Match = re.search("{Exp_[0-9]+", i)
        #     MatchedExp = Match.group(0)
        #     PoSID = MatchedExp[5:]
        else:
            PoSID = str(0)
        # if int(PoSID) > 0:
        # if "/" in PoS:
        #     PoSList = PoS.split('/')
        #     PoS = PoSList[int(PoSID)-1]
        #     print(WdID + "\t" + str(PoSID) + "\t" + MnID + "\t" + str(SID) + "\t" + Wd  + "\t" + PoS + "\t",end = "")
        if "/" in PoS:
            PoSList = PoS.split('/')
            print(WdID + "\t" + str(PoSID) + "\t" + MnID + "\t" + str(SID) + "\t" + Wd + "\t" + WdIPA  + "\t" + PoSList[int(PoSID)-1] + "\t", end="")
        else:
            print(WdID + "\t" + str(PoSID) + "\t" + MnID + "\t" + str(SID) + "\t" + Wd + "\t" + WdIPA  + "\t" + PoS + "\t", end = "")
        m = ""
        atta = 0
        for k in i:
            if k == "(":
                atta = 1
            elif k == ")":
                atta = 0
            if atta == 1:
                k = k.replace("。","{EOS}")
                k = k.replace("？","{EOS?}")
                k = k.replace("!","{EOS!}")
                k = k.replace("[","{SqBr}")
                k = k.replace("]","{/SqBr}")
            m = m + k
        # print(WdID + "\t" + str(PoSID) + "\t" + MnID + "\t" + str(SID) + "\t" + Wd  + "\t" + PoS + "\t",end = "")
        Sentences = re.split("(。|！|？|\{Break\})", m)             # 最近直したので動かないかも
        for j in Sentences:
#            j = re.sub("{PoS_[0-9]+}","",j)
            if re.match("[ァ-ヴふ⸢⸣～~　].+\[.+\]\(.+\)\Z", j):
                j = j.replace("[","\t[")
                j = j.replace("](","]\t(")
                # j = j.replace("{Break}","\n")
                print("\t", end="")
                p = j.replace(")、",")\n%s\t%s\t%d\t"%(WdID,Wd,SID+1))
                o = WdID + "\t" + Wd + "\t" + str(SID) + "\t" + p + "\n"
                out_file.write(o)
                SID = SID + 1
                if ")、" in j:
                    k = j.split(")、")
                    for l in k:
                        print(l + ")", end = "\t")
                    SID = SID + 1
                else:
                    print(j, end = "\t")
            else:
                print(j, end = "")
        print("\n", end = "")



out_file.close()



