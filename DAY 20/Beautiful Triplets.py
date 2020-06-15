n,d=map(int,input().split())
c=list(map(int,input().strip().split()))
gc=0
for i in range(n):
    if c[i]+d in c and c[i]+2*d in c:
        gc+=1
print (gc)
