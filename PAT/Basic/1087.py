n=int(input())
d={}
for i in range(1,n+1):
    d[i//2+i//3+i//5]=1
print(len(d))