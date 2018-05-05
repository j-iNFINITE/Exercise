# -*- coding: utf-8 -*-
#检测点2、5错误
n = int(input())
distance={}
diss=[int(e) for e in input().split(' ')]
for e in diss:
    if e not in distance.keys():
        distance[e]=1
    else:
        distance[e]+=1
days=0
temp=0
if len(distance.keys())==1:
    if sum(distance.values())==0:days=0
else:
    for i in sorted(distance.keys(),reverse=True):
        if days>i:
            days-=temp
            break
        temp=distance[i]
        days+=distance[i]
print(days)