# -*- coding: utf-8 -*-
#检测点4未通过
import re
low='abcdefghijklmnopqrstuvwxyz'
big=low.upper()
white=' '
code = input()
if code=='C':
    s=input()
    for e in low+big+white:
        patt=r'%s{2,}'%e
        poc=re.findall(patt,s)
        for x in poc:
            s=s.replace(x,'%s%s'%(len(x),x[0]))
if code=='D':
    s=input()
    for e in low+big+white:
        patt=r'\d+?%s'%e
        poc = re.findall(patt, s)
        for x in poc:
            s=s.replace(x,int(x[:-1])*x[-1])

print(s)