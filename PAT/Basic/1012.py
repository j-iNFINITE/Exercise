# -*- coding: utf-8 -*-
n = input().split(' ')
a1='N'
a2='N'
a2i=0
a3='N'
a4='N'
a4i=0
a5='N'

for i in n[1:]:
    i=int(i)
    flag=i%5
    if flag==0:
        if a1 == 'N' and i%2==0: a1 = 0
        if i%2==0:a1+=i
    if flag==1:
        if a2 == 'N': a2 = 0
        if a2i==0:
            a2+=i
        else:
            a2-=i
        if a2i==0:
            a2i=1
        else:
            a2i=0
    if flag==2:
        if a3 == 'N': a3 = []
        a3.append(i)
    if flag==3:
        if a4 == 'N': a4 = 0
        a4+=i
        a4i+=1
    if flag==4:
        if a5=='N':a5=0
        a5=max(a5,i)
if a3!='N':
    a3=len(a3)
if a4!='N':
    a4=round(a4/a4i,1)
print(' '.join(str(e) for e in [a1,a2,a3,a4,a5]))