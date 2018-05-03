# -*- coding: utf-8 -*-
#全部返回非零 找不出原因 用不用try···except···都一样 见鬼
import re
def cl(l):
    patt=r'\[(.+?)\]'
    res=re.findall(patt,l)
    return [e.strip() for e in res]
hands=cl(input())
eyes=cl(input())
mouth=cl(input())
n=int(input())
codes=[]
for i in range(n):
    codes.append([int(e)-1 for e in input().split(' ')])
for code in codes:
    breakflag=0
    for i in code:
        if i<0:
            print(r'Are you kidding me? @\/@')
            breakflag=1
            continue
    if breakflag==1:continue
    # try:
    #     print('%s(%s%s%s)%s' % (hands[code[0]], eyes[code[1]], mouth[code[2]], eyes[code[3]], hands[code[4]]))
    # except:
    #     print(r'Are you kidding me? @\/@')
    if code[0]>len(hands) or code[4]>len(hands):
        print(r'Are you kidding me? @\/@')
        continue
    elif code[1]>len(eyes) or code[3]>len(eyes):
        print(r'Are you kidding me? @\/@')
        continue
    elif code[3]>len(mouth) :
        print(r'Are you kidding me? @\/@')
        continue
    else:
        print('%s(%s%s%s)%s'%(hands[code[0]],eyes[code[1]],mouth[code[2]],eyes[code[3]],hands[code[4]]))