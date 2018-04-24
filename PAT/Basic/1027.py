# -*- coding: utf-8 -*-
n,s =[e for e in  input().split(' ')]
n=int(n)
linenum=0
z=1
if n <=7:
    print(s)
    print(n-1)
else:
    for i in range(3,1000,2):
        linenum+=1
        z+=2*i
        if z>=n:
            break
    linemax=linenum*2-1
    yy=0
    for i in range(linemax,0,-2):
        print(' '*int((linemax-i)/2)+s*i)  #审题要审清，后面不需要空格
        yy+=i
    for i in range(3,linemax+1,2):
        print(' ' * int((linemax - i) / 2) + s * i )
        yy+=i
    print(n-yy)