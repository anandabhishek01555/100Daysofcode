def firstRepeated(arr, n):
    j=0
    for i in range(n):
        c=arr[j]
        if arr.count(c)>1:
            return i+1
            break
        j+=1
        if j==n:
            return -1

n=int(input())
arr=list(map(int,input().split()))
print(firstRepeated(arr, n))