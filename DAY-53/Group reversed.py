N=int(input())
K=int(input())
A=list(map(int,input().split()))
i = 0
while(i < N):
    j = i + K
    A[i:j] = reversed(A[i:j])
    i += K
print(A)
