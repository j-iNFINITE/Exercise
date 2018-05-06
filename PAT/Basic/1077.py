# -*- coding: utf-8 -*-
n,up =[int(e) for e in input().split(' ')]
reasonable=list(range(up+1))
ans=[]
for i in range(n):
    temp=[int(e) for e in input().split(' ')]
    G2=temp[0]
    G1t=temp[1:]
    G1=[]
    for e in G1t:
        if e in reasonable:
            G1.append(e)
    G1.remove(max(G1))
    G1.remove(min(G1))
    all=sum(G1)/len(G1)+G2
    ans.append(all/2)

for e in ans:
    if int(e)<=e-0.5:
        print(int(e)+1)
    else:
        print(int(e))