# -*- coding: utf-8 -*-
h = input()
w=input()
flag=0
lost=[]
for e in w:
    if h.find(e)==-1:
        flag=1
        lost.append(e)
        h=h.replace(e, '', 1)
    else:
        h=h.replace(e,'',1)
if flag==0:
    print('Yes %s'%len(h))
else:
    print('No %s'%len(lost))
