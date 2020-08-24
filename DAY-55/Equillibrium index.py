def equi(a,n):
    t=sum(a)
    r=0
    for i in range(n-1,-1,-1):
        l=t-r-a[i]
        if l==r:
            return (i+1)
        r+=a[i]
    return -1

n=int(input())
a=list(map(int,input().split()))
print(equi(a,n))
