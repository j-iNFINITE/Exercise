# -*- coding: utf-8 -*-
def check(num):
    num=str(num)
    return num==num[::-1]
n=input()
count=0
while check(n)==False:
    new=int(n)+int(n[::-1])
    print('%s + %s = %s'%(n,n[::-1],new))
    n=str(new)
    if count>8:
        print('Not found in 10 iterations.')
        exit(0)
    count+=1
print('%s is a palindromic number.'%n)