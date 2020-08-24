n=int(input())
arr=list(map(int,input().split()))
m=arr[-1]
a=[]
for i in range(n-1,-1,-1):
    if arr[i]>=m:
        a.append(arr[i])
        m=arr[i]
print(a[::-1])
