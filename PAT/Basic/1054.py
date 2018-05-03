# -*- coding: utf-8 -*-
n = int(input())
legal=[e/100 for e in range(-100000,100001,1)]
ans=[]
for e in input().split(' '):
    try:
        if float(e) in legal:
            ans.append(float(e))
        else:
            print('ERROR: %s is not a legal number' % e)
    except:
        print('ERROR: %s is not a legal number' % e)
if len(ans)>1:
    print('The average of %s numbers is %.2f'%(len(ans),sum(ans)/len(ans)))
elif len(ans)==1:
    print('The average of 1 number is %.2f'%sum(ans))
else:
    print('The average of 0 numbers is Undefined')


