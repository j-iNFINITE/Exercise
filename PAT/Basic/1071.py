# -*- coding: utf-8 -*-
k,T =[int(e) for e in input().split(' ')]
turn=0
while turn <T:
    n1,b,t,n2=[int(e) for e in input().split(' ')]
    if t>k:
        print('Not enough tokens.  Total = %s.'%k)
        turn+=1
        continue
    if n1>n2:
        flag=0
    else:
        flag=1
    if b==int(flag):
        k+=t
        print('Win %s!  Total = %s.'%(t,k))
    else:
        k-=t
        if k<=0:
            print('Lose %s.  Total = 0.'%t)
            print('Game Over.')
            exit(0)
        print('Lose %s.  Total = %s.'%(t,k))
    turn+=1