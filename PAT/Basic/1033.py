# -*- coding: utf-8 -*-
miss= input()
raw=input()
if '+' in miss:
    raw=''.join([e for e in raw if e not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
    miss=miss.replace('+','')
for e in miss:
    e=e.upper()
    raw=raw.replace(e,'')
    e=e.lower()
    raw=raw.replace(e,'')

print(raw)