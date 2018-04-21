# -*- coding: utf-8 -*-
a,a1,b,b1 = input().split(' ')
sa=0
sb=0
an=len(a.split(a1))-1
bn=len(b.split(b1))-1
if an>0:
    sa=int(a1*an)
if bn>0:
    sb=int(b1*bn)
print(sa+sb)