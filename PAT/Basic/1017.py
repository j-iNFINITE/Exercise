# -*- coding: utf-8 -*-
a,b = input().split(' ')
q=int(a)//int(b)
r=int(a)%int(b)

print(' '.join([str(q),str(r)]))