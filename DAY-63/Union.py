a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(len(b)):
    if b[i] in a:
        print(i,end=" ")
        a.remove(b[i])
        print()
print(a)