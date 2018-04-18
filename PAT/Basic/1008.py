# -*- coding: utf-8 -*-
[n,m] = input().split(' ')
n=int(n)
m=int(m)
if m>n:m=m%n
line=input().split(' ')
print(' '.join((line*2)[n-m:2*n-m]),end='')
#监测点1不通过