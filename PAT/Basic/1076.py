# -*- coding: utf-8 -*-
n = int(input())
ans=[]
change={
    'A':1,
    'B':2,
    'C':3,
    'D':4,
}
for i in range(n):
    temp=input().split(' ')
    for e in temp:
        a,b=e.split('-')
        if b=='T':
            ans.append(change[a])
for i in ans:
    print(i,end='')