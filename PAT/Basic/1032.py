# -*- coding: utf-8 -*-
#不管哪种方法 最后一项都会超时
#方法一
n = int(input())
zf={}
for i in range(n):
    a,b=input().split(' ')
    b=int(b)
    if b==0:
        continue
    try:
        zf[a] += b
    except:
        zf[a]=b
maxzf=max(list(zf.values()))
nu=list(zf.keys())[list(zf.values()).index(maxzf)]

print(' '.join([str(nu),str(maxzf)]))

#方法二
# n = int(input())
# zf=[]
# for i in range(n):
#     a,b=[int(e) for e in input().split(' ')]
#     if b==0:
#         continue
#     if a>len(zf):
#         for e in range(len(zf),a):
#             zf.append(0)
#         zf[a-1]=b
#     else:
#         zf[a-1]+=b
# maxzf=max(zf)
# print(' '.join([str(zf.index(maxzf)+1),str(maxzf)]))
