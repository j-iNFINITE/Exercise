def bi(M,b):
    if M>b:return 'Gai'
    if M==b:return 'Ping'
    if M<b:return 'Cong'
M,X,Y=[int(e) for e in input().split(' ')]
for a in range(9,0,-1):
    flag=0
    for b in range(0,10):
        jia=10*a+b
        yi=10*b+a
        if abs(jia-yi)/X==yi/Y:
            bing=yi/Y
            flag=1
            break
    if flag==1:
        print(jia,bi(M,jia),bi(M,yi),bi(M,bing))
        exit()
print('No Solution')
