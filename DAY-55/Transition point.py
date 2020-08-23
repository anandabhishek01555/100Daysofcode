n=int(input())
arr=list(map(int,input().split()))
if arr.count(1)==n:
    print("0")
elif arr.count(0)==n:
    print("-1")
else:
    for i in range(n):
        if i < n-1:
            if arr[i]==0 and arr[i+1]==1:
                print(i+1)
                break