# -*- coding: utf-8 -*-
n = int(input())
q=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
errorid=[]
lastmod=[1,0,'X',9,8,7,6,5,4,3,2]
flag=0
for i in range(n):
    z=0
    try:
        l=input()
        nl=[int(e) for e in l[:-1]]
    except:
        errorid.append(l)
        continue
    for a,b in zip(q,nl):
        z+=a*b
    z=z%11
    last=lastmod[z]
    if str(last)!=str(l[-1]):
        errorid.append(l)
        flag=1

if flag==0:
    print('All passed')
else:
    for e in errorid:
        print(''.join([str(i) for i in e]))