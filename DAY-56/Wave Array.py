N=int(input())
A=list(map(int,input().split()))
for i in range(0,N,2):
    if (i<N-1 and A[i] < A[i+1]):
        A[i],A[i+1] = A[i+1],A[i]
print(A)