# -*- coding: utf-8 -*-
#检测点2错误
s = input().lower()
alp='0abcdefghijklmnopqrstuvwxyz'
all=0
for e in s:
    if e.isalpha():
        all+=alp.index(e)
binary=''
one=0
zero=0
if all==1:
    print('0 1')
elif all==0:
    print('1 0')
else:
    while all>=1:
        if all %2==1:
            one+=1
        else:
            zero+=1
        all=all//2
    print(' '.join([str(zero),str(one)]))