# -*- coding: utf-8 -*-
#测试点3超时
n = int(input())
paira={}
pairb={}
for i in range(n):
    a,b=input().split(' ')
    paira[a]=b
    pairb[b]=a
m=int(input())
dog=[]
come=input().split(' ')
for e in come:
    if e in paira.keys():
        if paira[e] not in come:
            dog.append(e)
    elif e in pairb.keys():
        if pairb[e] not in come:
            dog.append(e)
    else:
        dog.append(e)


print(len(dog))
if len(dog)>0:print(' '.join(sorted(dog))) #没狗的时候不返回