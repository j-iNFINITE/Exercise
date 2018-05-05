# -*- coding: utf-8 -*-
import functools
def r(a,b):
    return (a+b)/2
n = int(input())
robe=[int(e) for e in input().split(' ')]
robe=sorted(robe)


print(int(functools.reduce(r,robe)))