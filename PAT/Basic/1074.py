# -*- coding: utf-8 -*-
#检测点1、3未通过
ary = input()
a=int(input())
b=int(input())
temp=a+b
temp=str(temp).zfill(len(ary))
ans=[]
flag=0
for x,y in zip(temp[::-1],ary[::-1]):
    x=int(x)
    x += flag
    flag = 0
    y=int(y)
    if y ==0:
        ans.append(x)
    else:
        ans.append(x%y)
        flag=x//y
if flag!=0:ans.append(flag)
print(int(''.join([str(e) for e in ans])[::-1]))