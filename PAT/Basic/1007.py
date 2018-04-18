# -*- coding: utf-8 -*-
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
# rng=input()
# plist=[]
# count=0
# for n in primes():
#     if n <= int(rng):
#         print(n)
#         # plist.append(n)
#         # if n-2 in plist:
#         #     count+=1
#     else:
#         break
#  print(count)
#====================================================
# def getprimes(maxnum):
#     totallist=[e for e in range(0,maxnum)]
#     primes=[]
#     for e in range(2,len(totallist)):
#         if totallist[e]!=0:
#             primes.append(totallist[e])
#             f(totallist[e],totallist,maxnum)
#     return primes
# def f(prime,totalist,maxnum):
#     for e in range(2,int(maxnum/prime)+1):
#         if not prime*e>maxnum-1:
#             totalist[e*prime]=0
#====================================================
import math
def is_prime(number, primes):
    up_data = int(math.sqrt(number))
    for prime in primes:
        if prime > up_data:
            break
        if number % prime == 0:
            return False
    return True

up_limit = input()
up_limit = int(up_limit)
last_prime, next_prime = 2, 3
count = 0
primes = [2, 3]
if up_limit > 4:
    for number in range(5, up_limit+1):
        if is_prime(number, primes):
            primes.append(number)
            last_prime = next_prime
            next_prime = number
            if (next_prime - last_prime) == 2:
                count += 1

print(str(count))