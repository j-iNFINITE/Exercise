# -*- coding: utf-8 -*-
n = int(input())
anslist=[]
def to(raw):
    raw=int(raw)
    if raw==0: return 'tret'
    Blist='jan,feb,mar,apr,may,jun,jly,aug,sep,oct,nov,dec'.split(',')
    Alist='tam,hel,maa,huh,tou,kes,hei,elo,syy,lok,mer,jou'.split(',')
    A=raw//13
    if A>0:
        A=Alist[A-1]
    else:
        A=''
    B=raw%13
    if B>0:
        B=Blist[B-1]
    else:
        B=''
    return ' '.join([A,B]).strip()
def back(raw):
    raw=raw.split(' ')
    ans=0
    if raw=='tret': return '0'
    for e in raw:
        if e in 'jan,feb,mar,apr,may,jun,jly,aug,sep,oct,nov,dec'.split(','):
            ans+='jan,feb,mar,apr,may,jun,jly,aug,sep,oct,nov,dec'.split(',').index(e)+1
        if e in 'tam,hel,maa,huh,tou,kes,hei,elo,syy,lok,mer,jou'.split(','):
            ans+=('tam,hel,maa,huh,tou,kes,hei,elo,syy,lok,mer,jou'.split(',').index(e)+1)*13
    return ans
for i in range(n):
    raw=input()
    if raw.isnumeric():
        ans=to(raw)
    else:
        ans=back(raw)
    anslist.append(ans)

for e in anslist:
    print(e)