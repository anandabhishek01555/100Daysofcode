#code
t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    l=[]
    for i in range(n):
        if a[i]!=0:
            l.append(a[i])
    mul=len(a)-len(l)
    for i in range(mul):
        l.append(0)
    for i in l:
        print(i,end=" ")
    print()
    t-=1