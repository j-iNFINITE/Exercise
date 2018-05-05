# -*- coding: utf-8 -*-
#神他妈唬人
import math
n = int(input())
m=0
for i in range(n):
    a,b=[int(e) for e in input().split(' ')]
    m=max(math.sqrt(a*a+b*b),m)



print('%.2f'%m)