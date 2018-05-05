# -*- coding: utf-8 -*-
#检测点2未通过
import math
a,b,k = input().split(' ')
az,am=[int(e) for e in a.split('/')]
bz,bm=[int(e) for e in b.split('/')]
k=int(k)
z1=az*bm*k/(am*bm)
z2=am*bz*k/(am*bm)
if z1>z2:z1,z2=z2,z1

kzlist=range(math.ceil(z1),int(z2)+1)
result=[]
for e in kzlist:
    flag=0
    if e%k!=0:
        if e%2==0 and k%2==0:
            flag=1
        else:
            for i in range(min(e, k), 1, -1):
                if e % i == 0 and k % i == 0:
                    flag=1

        if flag==0:result.append('%s/%s'%(e,k))
print(' '.join(result))