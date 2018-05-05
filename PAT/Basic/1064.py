# -*- coding: utf-8 -*-
n = input()
friends={}
def fz(num):
    nums=[int(e) for e in num]
    return sum(nums)
for e in input().split(' '):
    friends[fz(e)]=0
print(len(friends))
print(' '.join([str(e) for e in sorted(friends.keys())]))