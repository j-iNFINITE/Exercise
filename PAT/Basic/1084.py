# -*- coding: utf-8 -*-
def poc(s):
    s=str(s)
    last=s[0]
    count=0
    ans=''
    for i in s:
        if i==last:
            count+=1
        else:
            ans=ans+last+str(count)
            last=i
            count=1
    ans=ans+last+str(count)
    return ans
d,n=[int(e) for e in input().split(' ')]
first=str(d)
turn=0
while turn<n-1:
    d=poc(d)
    turn+=1



print(d)