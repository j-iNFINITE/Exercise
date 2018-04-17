# -*- coding: utf-8 -*-
n=str(input())
hanzi=['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
ans=0
for e in n:
  ans=ans+int(e)
string=[]
for e in str(ans):
    string.append(hanzi[int(e)])
print(' '.join(string))