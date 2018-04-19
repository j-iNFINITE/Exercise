# -*- coding: utf-8 -*-
def getans(x,d):
    ans1=x*d
    ans2=d-1
    return ans1,ans2
n = input().split(' ')
ans=[]
for i in range(0,len(n),2):
    ans = []
    if int(n[i+1])==0:break
    [ans1,ans2]=getans(int(n[i]),int(n[i+1]))
    if int(n[i]) == 0: ans1=ans2=0
    ans.append(str(ans1))
    ans.append(str(ans2))
    print(' '.join(ans))