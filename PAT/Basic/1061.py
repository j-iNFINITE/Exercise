# -*- coding: utf-8 -*-
n,m =[int(e) for e in input().split(' ')]
scodict={}
order=0
final=[]
for e in input().split(' '):
    scodict[order]=int(e)
    order+=1
right=[int(e) for e in input().split(' ')]
for i in range(n):
    sco=0
    ans=[int(e) for e in input().split(' ')]
    s=[[e[0]+e[1] for e in zip(right,ans)]]
    anso=0
    for e in s[0]:
        if e!=1:
            sco+=scodict[anso]

        anso+=1
    final.append(sco)
for e in final:
    print(e)