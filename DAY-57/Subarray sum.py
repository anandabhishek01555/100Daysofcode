n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in range(n):
    for j in range(i+1,n+1):
        x=sum(arr[i:j])
        k.append(x)
print(max(k))
