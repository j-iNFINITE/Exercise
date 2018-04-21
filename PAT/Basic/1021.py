# -*- coding: utf-8 -*-
n = input()
ndict={}
for i in range(10):
    ndict['%s'%i]=0
for e in n:
    ndict[e]+=1
anslist=sorted(ndict.keys())
for e in anslist:
    if ndict[e]!=0:print('%s:%s'%(e,ndict[e]))
