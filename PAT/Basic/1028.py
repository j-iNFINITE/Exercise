# -*- coding: utf-8 -*-
#最后一个检测点超时，需要优化
n = int(input())
agemin=18140906
agemax=20140906
count=0
namelist=[]
ages=[]
for i in range(n):
    name,bir=input().split(' ')
    bir=int(''.join(bir.split('/')))
    if agemin<=bir<=agemax:
        namelist.append(name)
        ages.append(bir)
        count+=1
if count>0:
    youngest=namelist[ages.index(max(ages))]
    oldest=namelist[ages.index(min(ages))]
    print(' '.join([str(count),oldest,youngest]))
else:
    print('0')