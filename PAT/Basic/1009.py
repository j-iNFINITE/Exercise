# -*- coding: utf-8 -*-
n = input()
words=n.split(' ')
print(' '.join([words[e] for e in range(len(words)-1,-1,-1)]))