# -*- coding: utf-8 -*-
n = input().split('E')
change=int(n[1])
fh=n[0][0]
a,b=n[0][1:].split('.')
if change<0:
    ans='0'*(-change)+a+b
    ans=ans[0]+'.'+ans[1:]
else:
    if len(b)>change:
        ans=a+b
        ans=ans[:change+1]+'.'+ans[change+1:] #检测点四
    else:
        ans=a+b+'0'*(change-len(b))
        ans=int(ans)

if change==0:
    ans=n[0][1:]
if fh=='-':
    ans='-'+str(ans)
print(ans)