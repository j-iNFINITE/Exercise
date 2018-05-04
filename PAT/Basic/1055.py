# -*- coding: utf-8 -*-
#检测电3、4未通过
N,K = [int(e) for e in input().split(' ')]
peoples=[]
for i in range(N):
    name,height=input().split(' ')
    height=int(height)
    peoples.append([name,height])
peoples=sorted(peoples,key=lambda x:x[0])
peoples=sorted(peoples,key=lambda x:x[1])
lenqueue=[N//K]*(K-1)+[N%K+N//K]
queue=[]
for l in lenqueue:
    tempqueue=peoples[0:l]
    if len(peoples)!=l:peoples=peoples[l:]
    tempqueue=sorted(tempqueue,key=lambda x: x[1],reverse=True)
    sq=[tempqueue[0]]
    for i in range(1,l):
        if i%2==0:
            sq=sq+[tempqueue[i]]
        else:
            sq=[tempqueue[i]]+sq
    queue.append(sq)
for e in reversed(queue):
    print(' '.join([i[0] for i in e]))