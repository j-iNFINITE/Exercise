# -*- coding: utf-8 -*-
#检测点2答案错误
n = input()
n=n.lower()
ansdict={}
for i in 'abcdefghijklmnopqrstuvwxyz':
    ansdict[i]=0
for i in n:
    if i in ansdict.keys():
        ansdict[i]+=1
ans=list(ansdict.keys())[list(ansdict.values()).index(max(ansdict.values()))]
print('%s %s'%(ans,max(ansdict.values())))