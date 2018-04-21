# -*- coding: utf-8 -*-
A,B,D =[int(e) for e in input().split(' ')]
oringin=A+B
ans=''
if oringin==0:
    print(0)
else:
    while oringin!=0:
       ans=str(oringin%D)+ans
       oringin=oringin//D
    print(ans)