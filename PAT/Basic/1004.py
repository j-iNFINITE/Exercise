# -*- coding: utf-8 -*-
n = input()
maxs=0
maxl=[]
mins=100
minl=[]
for i in range(int(n)):
    line=input()
    line=line.split(' ')
    if int(line[2])>maxs:
        maxs=int(line[2])
        maxl=line
    if int(line[2])<mins:
        mins=int(line[2])
        minl=line
print(' '.join(maxl[0:2]))
print(' '.join(minl[0:2]))