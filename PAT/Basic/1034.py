# -*- coding: utf-8 -*-
def jh(ans,reverse=False):

    A=0
    flag=0
    # ans='-9/3'
    if ans.find('-')>-1:flag=1
    ans=ans.replace('-','')
    z,m=[int(e) for e in ans.split('/')]
    for i in range(min(z,m),1,-1):  #找最大公约数导致超时？
        if z%i==0 and m%i==0:
            z=z//i
            m=m//i
            break
    if z>=m:
        A=z//m
        z=z%m
    if z==0:
        B=''
    else:
        B='%s/%s'%(z,m)
    if A==0:A=''
    if reverse:flag-=1
    if flag==0:
        return ('%s %s'%(A,B)).strip()
    else:
        return ('(-'+('%s %s'%(A,B)).strip()+')').strip()

A,B = input().split(' ')
Az,Am=[int(e) for e in A.split('/')]
Bz,Bm=[int(e) for e in B.split('/')]
if Az==0:
    print('0'+' + '+jh(B)+' = '+jh(B))
    print('0'+' - '+jh(B)+' = '+jh(B,reverse=True))
    print('0'+' * '+jh(B)+' = '+'0')
    print('0'+' / '+jh(B)+' = '+'0')
elif Bz==0:
    print(jh(A)+' + '+'0'+' = '+jh(A))
    print(jh(A)+' - '+'0'+' = '+jh(A))
    print(jh(A)+' * '+'0'+' = '+'0')
    print(jh(A)+' / '+'0'+' = '+'Inf')
else:
    ans1=str(Az*Bm+Bz*Am)+'/'+str(Am*Bm)
    print(jh(A)+' + '+jh(B)+' = '+jh(ans1))
    ans2=str(Az*Bm-Bz*Am)+'/'+str(Am*Bm)
    print(jh(A)+' - '+jh(B)+' = '+jh(ans2))
    ans3=str(Az*Bz)+'/'+str(Am*Bm)
    print(jh(A)+' * '+jh(B)+' = '+jh(ans3))
    ans4=str(Az*Bm)+'/'+str(Am*Bz)
    print(jh(A)+' / '+jh(B)+' = '+jh(ans4))