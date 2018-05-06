# -*- coding: utf-8 -*-
#最后一个检查点超时
p,m,n =[int(e) for e in  input().split(' ')]
pdict={}
mdict={}
ndict={}
ans=[]
for i in range(p):
    a,b=input().split(' ')
    pdict[a]=int(b)
for i in range(m):
    a,b=input().split(' ')
    mdict[a]=int(b)
for i in range(n):
    a,b=input().split(' ')
    ndict[a]=int(b)
for name in sorted(pdict.keys()):
    psco=pdict[name]
    if psco<200:continue
    if name not in ndict.keys():continue
    Gn = ndict[name]
    try:
        Gm=mdict[name]
    except:
        Gm=-1
    if Gm>Gn:
        G=Gm*0.4+Gn*0.6
    else:
        G=Gn
    if G<60:continue
    if G-0.5>=int(G):
        G=int(G)+1
    else:
        G=int(G)
    ans.append([name,psco,Gm,Gn,G])
for e in sorted(ans,key=lambda e:e[4],reverse=True):
    print(' '.join([str(x) for x in e ]))