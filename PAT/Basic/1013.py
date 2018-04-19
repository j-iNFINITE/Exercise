# -*- coding: utf-8 -*-
#检测点2格式错误
import math
def is_prime(number, primes):
    up_data = int(math.sqrt(number))
    for prime in primes:
        if prime > up_data:
            break
        if number % prime == 0:
            return False
    return True
start,end=input().split(' ')
primes=[2,3,5,7,11,13]
p=15
flag=0
while len(primes)<=int(end):
    if is_prime(p,primes):
        primes.append(p)
    p+=2
if int(end)<=6:
    primes = [2,3,5,7,11,13]
neend=len(primes)%10
primes=primes[int(start)-1:int(end)]
for i in range(1,len(primes)//10+2):
    print(' '.join([str(e) for e in primes[10*(i-1):10*i]]))

