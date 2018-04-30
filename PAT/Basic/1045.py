# -*- coding: utf-8 -*-
#测试点1、测试点3 超时
n = input()
rawlist=[int(e) for e in input().split(' ')]
srawlist=sorted(rawlist)
ans=[]
for e in zip(rawlist,srawlist):
    A,B=e
    if A==B:
        pos=rawlist.index(A)+1
        if max(rawlist[:pos])==A:
            ans.append(A)

print(len(ans))
print(' '.join([str(e) for e in ans]))