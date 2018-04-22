# -*- coding: utf-8 -*-
#python3的四舍五入要注意
A,B = [int(e) for e in input().split(' ')]
if (B-A)%100>=50:
    s=int((B-A)/100)+1
else:
    s=int((B-A)/100)
hh = s/ 3600
mm = (s % 3600) / 60
ss = s % 60
print('%02d:%02d:%02d'%(hh,mm,ss))