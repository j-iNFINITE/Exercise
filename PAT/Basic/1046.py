# -*- coding: utf-8 -*-
n = int(input())
Alose=0
Blose=0
for i in range(n):
    A,AA,B,BB=[int(e) for e in input().split(' ')]
    if AA==BB:continue
    correct=A+B
    if AA==correct:Blose+=1
    if BB==correct:Alose+=1

print('%s %s'%(Alose,Blose))