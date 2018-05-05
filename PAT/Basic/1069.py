# -*- coding: utf-8 -*-
m,n,s =[int(e) for e in  input().split(' ')]
s=s-1
waitlist=[]
for i in range(m):
    waitlist.append(input())
ans=[]
while s<m:
    p=waitlist[s]
    if p not in ans:
        ans.append(p)
        s+=n
    else:
        s+=1

if ans==[]:
    print('Keep going...')
else:
    for e in ans:
        print(e)