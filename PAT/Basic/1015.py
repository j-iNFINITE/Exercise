# -*- coding: utf-8 -*-
#花了两个小时 还是超时 GG
N,L,H = [int(e) for e in input().split(' ')]
parti=[]
partii=[]
partiii=[]
partiv=[]
for i in range(N):
    no,d,c=[int(e) for e in input().split(' ')]
    if d<L or c<L:
        continue
    elif d>=H and c>=H:
        parti.append([no,d,c,d+c])
    elif d>=H:
        partii.append([no,d,c,d+c])
    elif d>=c:
        partiii.append([no,d,c,d+c])
    else:
        partiv.append([no,d,c,d+c])
def sortpart(part):
    part=sorted(part,key=lambda x:x[0])
    part=sorted(part,key=lambda x:(x[3],x[1]),reverse=True)
    return part
ans=sortpart(parti)+sortpart(partii)+sortpart(partiii)+sortpart(partiv)
print(len(ans))
for e in ans:
    print(' '.join([str(i) for i in e[:3]]))