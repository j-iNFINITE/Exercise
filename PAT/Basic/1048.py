# -*- coding: utf-8 -*-
#检测点2、5 报错
A,B =input().split(' ')
cstring='0123456789JQK'
A=list(reversed(A))
B=list(reversed(B))
Ciphertext=[]
if len(A)<len(B):
    extra=B[len(A):]
    extra.reverse()
flag=1
for e in zip(A,B):
    a,b=[int(i) for i in e]
    if flag%2==0:
        b=b-a
        if b<0:b=b+10
    else:
        b=cstring[int((a+b))%13]
    Ciphertext.append(b)
    flag+=1
Ciphertext.reverse()
if 'extra'  in vars(): Ciphertext=extra+Ciphertext
print(''.join([str(e) for e in Ciphertext]))