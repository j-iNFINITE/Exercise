# -*- coding: utf-8 -*-
n,c = input().split(' ')
n=int(n)
if n%2==0:
    row=n/2
else:
    row=n/2+1
row=int(row)
for i in range(row):
    if i==0 or i==row-1:
        print(c*n)
    else:
        print(c+' '*(n-2)+c)