# -*- coding: utf-8 -*-
import re
n = int(input())
ans = []
for i in range(n):
    pw=input()
    if len(pw)<6:
        ans.append('Your password is tai duan le.')
        continue
    patt=r'[^a-zA-Z0-9/.]'
    if re.findall(patt,pw)!=[]:
        ans.append('Your password is tai luan le.')
        continue
    zm=r'[a-zA-z]'
    if re.findall(zm,pw)==[]:
        ans.append('Your password needs zi mu.')
        continue
    sz=r'[0-9]'
    if re.findall(sz,pw)==[]:
        ans.append('Your password needs shu zi.')
        continue
    ans.append('Your password is wan mei.')
for e in ans:
    print(e)
