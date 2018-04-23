# -*- coding: utf-8 -*-
n,s =[e for e in  input().split(' ')]
n=int(n)

for i in range(1,500,2):
    if 2*i+1>=n:
        z=2*(i-1)+1
        y=n-z
        countline=i-2-2
        break
for e in range(countline,0,-2):
    print(' '*int(((countline-e)/2))+s*e+' '*int(((countline-e)/2)))
for e in range(1,countline+1,2):
    if e==1:continue
    print(' ' * int(((countline - e) / 2)) + s * e + ' ' * int(((countline - e) / 2)))
print(y)