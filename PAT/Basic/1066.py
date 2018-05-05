# -*- coding: utf-8 -*-
m,n,a,b,h =[int(e) for e in  input().split(' ')]
hr=list(range(a,b+1))
result=[]
for i in range(m):
    temp=[int(e) for e in input().split()]
    new=[]
    for e in temp:
        if e in hr:
            e=h
        new.append(str(e).zfill(3))
    result.append(' '.join(new))
for e in result:
    print(e)