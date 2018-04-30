# -*- coding: utf-8 -*-
n = input()
def get(*list):
    for e in list:
        if e==None:
            print('',end='')
        else:
            print(e,end='')
Plist=[]
Alist=[]
Tlist=[]
elist=[]
slist=[]
tlist=[]
for i in n:
    if i=='P':Plist.append(i)
    if i=='A':Alist.append(i)
    if i=='T':Tlist.append(i)
    if i=='e':elist.append(i)
    if i=='s':slist.append(i)
    if i=='t':tlist.append(i)
maxlen=max(len(Plist),len(Alist),len(Tlist),len(elist),len(slist),len(tlist))
if len(Plist)<maxlen:Plist+=['']*(maxlen-len(Plist))
if len(Alist)<maxlen:Alist+=['']*(maxlen-len(Alist))
if len(Tlist)<maxlen:Tlist+=['']*(maxlen-len(Tlist))
if len(elist)<maxlen:elist+=['']*(maxlen-len(elist))
if len(slist)<maxlen:slist+=['']*(maxlen-len(slist))
if len(tlist)<maxlen:tlist+=['']*(maxlen-len(tlist))
for e in zip(Plist,Alist,Tlist,elist,slist,tlist):
    print(''.join(e),end='')