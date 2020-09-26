t=int(input())
while(t>0):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    x=min(l)
    print(k-x)
    t-=1