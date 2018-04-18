# -*- coding: utf-8 -*-
n = input()
ge=''.join([str(e) for e in range(1,10)])
if n[-1]=='0':
    partiii=''
else:
    partiii=''.join(ge[:int(n[-1])])
if len(n)>1:
    partii='S'*int(n[-2])
else:
    partii=''
if len(n)>2:
    parti='B'*int(n[-3])
else:
    parti=''
print(parti+partii+partiii)