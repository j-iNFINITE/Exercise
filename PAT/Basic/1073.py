# -*- coding: utf-8 -*-
#和1058不是差不多么，连输入样例都一样=-=
#检测点2、3没通过
import re
patt=r'\((.+?)\)'
N,M =[int(e) for e in  input().strip().split(' ')]
quesco={}
quechoices={}
queans={}
queerror={}
sco=[]
newerrors={}
for i in range(M):
    tempst=input().split(' ')
    quesco[i+1]=float(tempst[0])
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
        if int(quechoices[order])>=int(e[0]) :
            if queans[order]!=e[1:]:
                if len([i for i in e[1:] if i not in queans[order]])==0:
                    finalsco += quesco[order]*0.5
            else:
                finalsco+=quesco[order]
        else:
            queerror[order]+=1
        for x in [i for i in e[1:] if i not in queans[order]]:
            try:
                newerrors['%s-%s'%(order,x)]+=1
            except:
                newerrors['%s-%s' % (order, x)] = 1
        for x in [i for i in queans[order] if i not in e[1:]]:
            try:
                newerrors['%s-%s'%(order,x)]+=1
            except:
                newerrors['%s-%s' % (order, x)] = 1
        order+=1
    sco.append(finalsco)
for i in sco:
    print(i)
if len(newerrors)==0:
    print('Too simple')
else:
    maxerror=max(newerrors.values())
    errors=[]
    errors.append(str(maxerror))
    for i in sorted(newerrors.keys()):
        if newerrors[i]==maxerror:
            print(' '.join([str(maxerror),str(i)]))