# -*- coding: utf-8 -*-
n = int(input())
flag=[]
for i in range(n):
    a,b,c=input().split(' ')
    if int(a)+int(b)>int(c):
        flag.append(1)
    else:
        flag.append(0)

num=1
for e in flag:
    if e==0:
        print('Case #%s: false'%num)
    else:
        print('Case #%s: true'%num)
    num+=1