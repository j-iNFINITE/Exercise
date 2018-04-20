# -*- coding: utf-8 -*-
#有几个检查点返回格式错误，没找到原因
m1 = input()
m2 = input()
m3 = input()
m4 = input()
ans=[]
posi=0
string='0123456789ABCDEFGHIJKLMN'
flag=0
for e in zip(m1,m2):
    t1,t2=e
    if t1==t2 and t1.isupper() and t1.isalpha() and flag==0:
        ans.append(t1)
        flag=1
        continue
    if t1==t2 and flag==1:
        ans.append(t1)
    if len(ans)==2:break
for e in zip(m3,m4):
    t1,t2=e
    if t1==t2 and t1.isalpha() :
        ans.append(posi)
    posi+=1
weeklist=['MON','TUE','WED','THU','FRI','SAT','SUN']
print('%s %02d:%02d'%(weeklist[string.index(ans[0])-10],string.index(ans[1]),ans[2]))