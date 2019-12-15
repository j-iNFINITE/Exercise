a,b=[int(e) for e in input().split(' ')]
print(str(a*b)[::-1].lstrip('0')) #不能0开头