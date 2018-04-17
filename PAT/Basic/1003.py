# -*- coding: utf-8 -*-
n = input()
for i in range(int(n)):
    line=input()
    flag = 0
    if len(line)<3:
        print('NO')
        continue
    if line=='PAT' or line=='PAAT':
        print('YES')
        continue
    for s in line:
        if s =='P' or s =='A' or s =='T':
            pass
        else:
            print('NO')
            flag=1
            break
    if flag==1:continue
    sp=line.replace('P',',').replace('T',',')
    sp=sp.split(',')
    if (len(sp[0])*len(sp[1])==len(sp[2])) and line.index('P')<line.index('T'): #这题考的是阅读理解
        print('YES')
    else:
        print('NO')