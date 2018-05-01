# -*- coding: utf-8 -*-
n = int(input())
winner={}
for i in range(n):
    team,score=input().split(' ')
    team=team.split('-')[0]
    score=int(score)
    if team not in winner.keys():
        winner[team]=score
    else:
        winner[team]+=score

maxscore=max(winner.values())
print('%s %s'%(list(winner.keys())[list(winner.values()).index(maxscore)],maxscore))