def immediateSmaller(arr,n,x):
    m=[]
    k=[]
    for i in range(n):
        if min(arr)==x:
            return -1
            break
        else:
            if arr[i]<x:
                m.append(arr[i])
                
    for i in range(len(m)):
        d=x-m[i]
        k.append(m[i])
    return max(k)
    
n=int(input())
arr=list(map(int,input().split()))
x=int(input())
print(immediateSmaller(arr, n, x))