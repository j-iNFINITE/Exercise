# -*- coding: utf-8 -*-
n = int(input())
f=[int(e) for e in input().split(' ')]
ans={}
for i in range(n):
    try:
        ans[abs(f[i]-i-1)]+=1
    except:
        ans[abs(f[i] - i - 1)] =1
for e in sorted(ans.keys(),reverse=True):
    if ans[e]==1:continue
    print('%s %s'%(e,ans[e]))