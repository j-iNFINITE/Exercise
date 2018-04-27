# -*- coding: utf-8 -*-
n = int(input())
sl=[int(e) for e in input().split(' ')]
search=[int(e) for e in input().split(' ')[1:]]
ansl=[0]*101 #百分制 0到100
for e in sl:
    ansl[e]+=1
search=[str(ansl[e]) for e in search]
print(' '.join(search))