def equilibriumPoint(A, N):
    total = sum(A)
    r = 0
    for i in range(N-1, -1, -1):
        l = total - r - A[i]
        if l==r:
            return(i+1)
        r += A[i]
    return -1

N = int(input())
A = [int(x) for x in input().strip().split()]
print(equilibriumPoint(A, N))