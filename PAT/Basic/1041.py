# -*- coding: utf-8 -*-
n = int(input())
ksdict={}
for i in range(n):
    zkz,sj,ks=input().split(' ')
    ksdict[sj]=[zkz,ks]
checknum=int(input())
for i in input().split(' '):
    print(' '.join(ksdict[i]))