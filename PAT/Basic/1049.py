# -*- coding: utf-8 -*-
n = int(input())

ans=0
mu=[]
for e in zip(range(1,n+1),reversed(range(1,n+1))):
    mu.append(e[0]*e[1])
raw=[float(e) for e in input().split(' ')]
cd=len(raw)
for i in range(cd):
    ans+=raw[i]*mu[i]

print('%.2f'%ans)