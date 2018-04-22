# -*- coding: utf-8 -*-
n =[int(e) for e in  input().split(' ')]
ans=''
for i in range(1,10):
    ans=ans+str(n[i]*str(i))
ans=ans[0]+str(0)*n[0]+ans[1:]
print(ans)