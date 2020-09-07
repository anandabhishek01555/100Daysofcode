a=list(map(int,input().split()))
res=1
for i in range(len(a)):
    if a[i]<=res:
        res+=a[i]
    else:
        break
print(res)
