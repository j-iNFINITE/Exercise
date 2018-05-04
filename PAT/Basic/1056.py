# -*- coding: utf-8 -*-
N =[int(e) for e in  input().split(' ')]
nums=N[1:]
N=N[0]
ansl=[]
for i in range(N-1):
    for j in range(i+1,N):
        if nums[i]*10+nums[j] not in ansl:
            ansl.append(nums[i]*10+nums[j])
        if nums[i]+nums[j]*10 not in ansl:
            ansl.append(nums[i]+nums[j]*10)



print(sum(ansl))