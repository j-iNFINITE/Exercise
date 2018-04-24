# -*- coding: utf-8 -*-
#检测点3返回非零 找不出原因
n,p =[int(e) for e in  input().split(' ')]
l=[int(e) for e in input().split(' ')]
if max(l)<=min(l)*p or n ==1:
    print(n)
else:
    lmax=max(l)
    nl=[e*p for e in l]
    nl.append(lmax)
    maxlen=len(nl)-sorted(nl).index(lmax)-1
    #通过数列方式仅适用于确定最大项的情况
    l=sorted(l)
    for i in range(n):
        lmin=l[i]*p
        if i+maxlen>=n:
            break
        for j in range(i+maxlen,n):
            if l[j]<=lmin:
                maxlen+=1
            else:
                break
    print(maxlen)
exit(0)