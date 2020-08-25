N=int(input())
A=list(map(int,input().split()))
s=int(input())
s1=0
for i in range(0,N+1):
    for j in range(1,N+1):
        s1=sum(A[i:j])
        if s1==s:
            print(i+1,j)
            break
    if s1==s:
        break