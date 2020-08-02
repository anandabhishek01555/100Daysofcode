t=int(input())
for _ in range(t):
    n=int(input())
    cnt=10
    a=[]
    for i in range(n):
        x=[]
        for j in range(i):
            x.append("**")
        for j in range(i,n):
            x.append(str(cnt))
            cnt+=10
        a.append(x)
    print(a)
    for i in range(n-1,-1,-1):
        x=[]
        for j in range(i,n):
            x.append(str(cnt))
            cnt+=10
        a[i].extend(x)
    print("Case #"+str(_+1))
    for i in a:
        x=''.join(i)
        print(x[:-1])





    

