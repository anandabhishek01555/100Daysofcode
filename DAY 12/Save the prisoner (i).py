t=int(input())
while t>0:
    n,m,s=map(int,input().split())
    a=s+m-1
    if(a>n):
        if(a%n==0):
            print(n)
        else:
            print(a%n)
    else:
        print(a)
    t-=1
