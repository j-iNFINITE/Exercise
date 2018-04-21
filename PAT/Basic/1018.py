# -*- coding: utf-8 -*-
#最后一个检测点超时
n = int(input())
win=[]
draw=[]
lose=[]
def check(a,b):
    if a==b:
        draw.append([a,b])
    if a=='C' and b=='J':win.append([a,b])
    if a=='C' and b=='B':lose.append([a,b])
    if a=='J' and b=='B':win.append([a,b])
    if a=='J' and b=='C':lose.append([a,b])
    if a=='B' and b=='C':win.append([a,b])
    if a=='B' and b=='J':lose.append([a,b])
for i in range(n):
    a,b=input().split(' ')
    check(a,b)
print(len(win),len(draw),len(lose))
print(len(lose),len(draw),len(win))
cwin=0
jwin=0
bwin=0
for e in win:
    a,b=e
    if a=='C':cwin+=1
    if a=='J':jwin+=1
    if a=='B':bwin+=1
maxwin=['B','C','J'][[bwin,cwin,jwin].index(max(bwin,cwin,jwin))]
close=0
jlose=0
blose=0
for e in lose:
    a,b=e
    if b=='C':close+=1
    if b=='J':jlose+=1
    if b=='B':blose+=1
maxlose=['B','C','J'][[blose,close,jlose].index(max(blose,close,jlose))]
print(maxwin,maxlose)