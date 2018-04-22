# -*- coding: utf-8 -*-
#应该还有几个情况没考虑到 3各测试点没过
start,n,point = (lambda x:[x[0],int(x[1]),int(x[2])]) ( input().split(' '))
data={}
orderpoint={}


def orderlist(start):
    ne=0
    rightdict={}
    while start!='-1':
        rightdict[ne]=start
        start=orderpoint[start]
        ne+=1
    return rightdict
if n==1:
    n=input()
    print(n)
else:
    for i in range(n):
        Address,Data,Next=input().split(' ')
        data[Address]=Data
        orderpoint[Address]=Next
    olddict=orderlist(start)
    neworder=list(range(n))
    neworder=sorted(neworder[:point],reverse=True)+neworder[point:]
    for e in neworder:
        try:
            print(' '.join([olddict[e],data[olddict[e]],olddict[neworder[neworder.index(e)+1]]]))
        except:
            print(' '.join([olddict[e], data[olddict[e]], '-1']))

