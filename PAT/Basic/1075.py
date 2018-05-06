# -*- coding: utf-8 -*-
#检测点5超时
start,n,k = input().split(' ')
n=int(n)
k=int(k)
address={}
parti=[]
partii=[]
partiii=[]
for i in range(n):
    Address,Data,Next=input().split(' ')
    address[Address]=[Data,Next]
while start!='-1':
    data,ne=address[start]
    data=int(data)
    if data<0:
        parti.append([start,data])
    elif data<=k:
        partii.append([start,data])
    else:
        partiii.append([start,data])
    start=ne
ans=parti+partii+partiii
if len(ans)>1:
    for i in range(len(ans)):
        if i==len(ans)-1:
            print(' '.join([str(e) for e in ans[i]]),end=' -1')
            break
        print(' '.join([str(e) for e in ans[i]]),end=' ')
        print(ans[i+1][0])
else:
    print(' '.join([str(e) for e in ans[i]]), end=' -1')