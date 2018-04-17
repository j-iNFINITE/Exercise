# -*- coding: utf-8 -*-
n=int(input())
steps=0
while n!=1:
    if n%2==1 :
        n=(3*n+1)/2
    else :
        n=n/2
    steps=steps+1
print(steps)