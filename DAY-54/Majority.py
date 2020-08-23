x,y=map(int,input().split())
arr=list(map(int,input().split()))
c1 = c2 = 0
c1=arr.count(x)
c2=arr.count(y)
if c1 > c2:
    print(x)
elif c2 > c1:
    print(y)
else:
    print(min(x,y))