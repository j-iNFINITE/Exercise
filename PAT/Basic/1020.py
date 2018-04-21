# -*- coding: utf-8 -*-
kinds,goal = [float(e) for e in input().split(' ')]
inventorys=[float(e) for e in input().split(' ')]
maxsell=[float(e) for e in input().split(' ')]
proslist=sorted([(lambda x:  [x[0],x[1],x[1]/x[0]]) (x) for x in list(zip(inventorys,maxsell))],key=lambda x:x[2],reverse=True) #lambda真好用
ans=0
sold=0
for e in proslist:
    if goal-e[0]<0:
        ans+=e[2]*goal
        break
    ans+=e[1]
    goal-=e[0]
print('%.2f'%float(ans))

