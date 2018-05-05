# -*- coding: utf-8 -*-
#检测点4超时
def numic(x):
    return x.isnumeric()
m,n,tol =[int(e) for e in  input().split(' ')]
datas=[]
dup={}
for i in range(n):
    temp=input()
    temp=temp.replace('\t',' ')
    temp=filter(lambda x:x.isnumeric(),[e  for e in temp.split(' ')])
    a=list(temp)
    for e in a:
        try:
            dup[e]+=1
        except:
            dup[e]=1
    datas.append([int(e) for e in a])
ans=[]
dupl=[]
for e in dup.keys():
    if dup[e]==1:
        dupl.append(e)
for i in range(n):
    for j in range(m):
        diff=[]
        point=datas[i][j]
        if i>0:
            diff.append(datas[i-1][j])
            if j>0:
                diff.append(datas[i-1][j-1])
            if j<m-1:
                diff.append(datas[i-1][j+1])
        if j>0:
            diff.append(datas[i][j-1])
        if j<m-1:
            diff.append(datas[i][j+1])
        if i<n-1:
            diff.append(datas[i+1][j])
            if j>0:
                diff.append(datas[i+1][j-1])
            if j<m-1:
                diff.append(datas[i+1][j+1])
        flag=0
        for e in diff:
            if abs(e-point)<=tol:
                flag=1
        if flag==0 and str(point) in dupl:
            ans.append('(%s, %s): %s'%(j+1,i+1,point))
        if len(ans)>1:
            print('Not Unique')
            exit(0)

if len(ans)==0:
    print('Not Exist')
else:
    print(ans[0])
