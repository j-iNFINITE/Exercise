# -*- coding: utf-8 -*-
import math
n = int(input())
result={}
for i in range(n):
    name,x,y=input().split(' ')
    x=abs(int(x))
    y=abs(int(y))
    result[name]=math.sqrt(x*x+y*y)

loser=list(result.keys())[list(result.values()).index(max(result.values()))]
winner=list(result.keys())[list(result.values()).index(min(result.values()))]
print(' '.join([winner,loser]))