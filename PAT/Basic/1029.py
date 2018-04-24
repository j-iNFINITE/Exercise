# -*- coding: utf-8 -*-
s1=''
s2={}
temps=input()
for e in  input():
    s2[e.upper()]=''
for e in temps:
    if e.upper() not in list(s2):
        if e.upper() not in s1:
            s1+=e.upper()


print(s1)