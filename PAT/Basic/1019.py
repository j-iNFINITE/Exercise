# -*- coding: utf-8 -*-
n = str('%04d'%int(input())) #注意输入值区间
if n=='6174':
    print('7641 - 1467 = 6174')
def bsort(n):
    return ''.join(sorted(list(str(n))))
def asort(n):
    return ''.join(sorted(list(str(n)),reverse=True))
if n[0]==n[1]==n[2]==n[3]:
    print('%s - %s = %s'%(n,n,'0000'))
else:
    while n!='6174':
        ans=int(asort(n))-int(bsort(n))
        print('%s - %s = %04d'%(asort(n),bsort(n),ans)) #其实一开始全部用%04d还更简单
        n=str('%04d'%ans)

