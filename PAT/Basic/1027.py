# -*- coding: utf-8 -*-
n,s =[e for e in  input().split(' ')]
n=int(n)

for i in range(1,500,2):
    if 2*i+1>=n:
        z=2*(i-1)+1
        y=n-z
        break
print(y,z)
z1=(z+1)/2
parti=[]
i=1
while z1!=0:
    parti.append(i)
    z1-=i
    i+=2
linemax=parti[-1]
for e in sorted(parti,reverse=True):
    print(' '*int((linemax-e)/2)+e*s+' '*int((linemax-e)/2))
for e in parti:
    if parti.index(e)==0:continue
    print(' ' * int((linemax - e) / 2) + e * s + ' ' * int((linemax - e) / 2))
if y!=0:
    print(y)