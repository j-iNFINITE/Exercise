# -*- coding: utf-8 -*-
A,P = input().split(' ')
def down(A):
    g,s,k=[int(e) for e in A.split('.')]
    K=g*17*29+s*29+k
    return K
def up(A):
    flag=0
    if A<0:
        flag=1
        A=-A
    g=A//(17*29)
    rem=A%(17*29)
    s=rem//29
    k=rem%29
    if flag==1:
        return '-'+'.'.join([str(e) for e in [g,s,k]])
    else:
        return '.'.join([str(e) for e in [g,s,k]])
ans=down(P)-down(A)
print(up(ans))