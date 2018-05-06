# -*- coding: utf-8 -*-
#检测点4、5超时
n = int(input())
dwcount={}
rank={}
dwsco={}
for i in range(n):
    code,sco,dw=input().split(' ')
    sco=int(sco)
    dw=dw.lower()
    try:
        dwcount[dw]+=1
    except:
        dwcount[dw]=1
    kind=code[0]
    if kind=='B':
        sco=int(sco/1.5)
    elif kind=='T':
        sco=int(sco*1.5)
    try:
        dwsco[dw]+=sco
    except:
        dwsco[dw]=sco

print(len(dwcount.keys()))
rankcount=1
for i in sorted(dwsco.values(),reverse=True):
    if i in rank.keys():
        rankcount+=1
        continue
    rank[i]=rankcount
    rankcount+=1
ans=[]
for dw in dwcount.keys():
    s=dwsco[dw]
    r=rank[s]
    c=dwcount[dw]
    ans.append([r,dw,s,c])
ans=sorted(ans,key=lambda x:[x[0],x[3],x[1]])
for e in ans:
    print(' '.join([str(i) for i in e]))