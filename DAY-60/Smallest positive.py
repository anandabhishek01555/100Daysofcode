def sol(a):
    m=max(a)
    if m<0:
        return 1
    if len(a)==1:
        return 2 if a[0]==1 else 1
    l=[0]*m
    for i in range(len(a)):
        if a[i]>0:
            if l[a[i]-1]!=1:
                l[a[i]-1]=1
    print(l)
    for i in range(len(l)):
        if l[i]==0:
            return i+1
    return i+2

a=list(map(int,input().split()))
print(sol(a))