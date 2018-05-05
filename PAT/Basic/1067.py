# -*- coding: utf-8 -*-
pw,count = input().split(' ')
count=int(count)
fool=0
while fool<count:
    newinput=input()
    if newinput=='#':exit(0)
    if newinput==pw:
        print('Welcome in')
        exit(0)
    else:
        print('Wrong password: %s'%newinput)
    fool+=1
print('Account locked')