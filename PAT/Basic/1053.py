# -*- coding: utf-8 -*-
def may(l):
    flag=k/2
    for i in l:
        i=float(i)
        if i<e:
            flag-=1
        if flag<0: return True
    return False
n,e,D =[e for e in  input().split(' ')]
n=int(n)
e=float(e)
D=int(D)
maybe=0
yes=0
for i in range(n):
    l=input().split(' ')
    k=int(l[0])
    watch=l[1:]
    if may(watch):
        if k>D:
            yes+=1
        else:
            maybe += 1


print('%.1f%% %.1f%%'%(maybe/n*100,yes/n*100))