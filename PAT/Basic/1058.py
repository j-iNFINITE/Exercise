# -*- coding: utf-8 -*-
import re
patt=r'\((.+?)\)'
N,M =[int(e) for e in  input().strip().split(' ')]
quesco={}
quechoices={}
queans={}
queerror={}
sco=[]
for i in range(M):
    tempst=input().split(' ')
    quesco[i+1]=int(tempst[0])
    quechoices[i+1]=int(tempst[2])
    queans[i+1]=tempst[3:]
    queerror[i+1]=0
for i in range(N):
    finalsco=0
    st=input()
    ans=re.findall(patt,st)
    order=1
    for e in ans:
        e=e.split(' ')
        if str(quechoices[order])==e[0] and queans[order]==e[1:]:
            finalsco+=quesco[order]
        else:
            queerror[order]+=1

        order+=1
    sco.append(finalsco)
for i in sco:
    print(i)
maxerror=max(queerror.values())
if maxerror==0:
    print('Too simple')
else:
    errors=[]
    errors.append(str(maxerror))
    for i in sorted(queerror.keys()):
        if queerror[i]==maxerror:
            errors.append(str(i))
    print(' '.join(errors))