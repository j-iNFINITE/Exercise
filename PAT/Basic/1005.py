# -*- coding: utf-8 -*-
num=input()
checklist=input().split(' ')
def getcheck(n):
    ans=[n]
    while n!=1:
        if n % 2 == 1:
            ans.append(int((3 * n + 1) / 2))
            n = (3 * n + 1) / 2

        else:
            ans.append(int(n / 2))
            n = n / 2

    return ans
checkdict={}
for e in checklist:
    checkdict[int(e)]=getcheck(int(e))
alllist=sorted(checkdict.values(),key=lambda x: len(x))
rng=1
result=[alllist[-1]]
for e in alllist[:-1]:
    inflag=1
    for i in alllist[rng:len(alllist)]:
        if [q for q in e if q not in i]==[]:
            inflag=0
    if inflag==1:
        result.append(e)
    inflag = 1
    rng+=1
real=[]
for e in result:
    real.append(list(checkdict.keys())[list(checkdict.values()).index(e)])
print(' '.join([str(e) for e in sorted(real,reverse=True)]))