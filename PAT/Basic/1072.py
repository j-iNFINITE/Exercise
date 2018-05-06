# -*- coding: utf-8 -*-
n,m =[int(e) for e in input().split(' ')]
illegal=input().split(' ')
checkresult=[]
confiscatecount=0
for i in range(n):
    confiscate=[]
    temp=input().split(' ')
    name=temp[0]
    staff=temp[2:]
    for e in staff:
        if e in illegal:
            confiscate.append(e)
            confiscatecount+=1
    if len(confiscate)>0:
        checkresult.append('%s: '%name+' '.join(confiscate))
for e in checkresult:
    print(e)
print(' '.join([str(e) for e in [len(checkresult),confiscatecount]]))