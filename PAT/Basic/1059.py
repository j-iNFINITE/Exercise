# -*- coding: utf-8 -*-
#检测点1、2超时 要用筛表法求质数？
import math
def prime(order):
    if order==2:return True
    for i in range(2,int(math.sqrt(order))+1):
        if order%i==0:
            return False
    return True
def check(W):
    if W not in order: return "%s: Are you kidding?" % W
    if W in checked: return "%s: Checked"%W
    if order.index(W)==0:return "%s: Mystery Award"%W
    if prime(order.index(W)+1):return "%s: Minion"%W
    return "%s: Chocolate"%W
N = int(input())
order=[]
for i in range(N):
    order.append(input())
outlist=[]
M = int(input())
checked=[]
for i in range(M):
    waitcheck=input()
    outlist.append(check(waitcheck))
    checked.append(waitcheck)

for e in outlist:
    print(e)