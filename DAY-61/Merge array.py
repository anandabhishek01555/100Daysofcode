a=list(map(int,input().split()))
b=list(map(int,input().split()))
n=len(a)
m=len(b)
for i in range(m):
    a.append(b[i])
a=sorted(a)
b.clear()
b=a[n:]
a=a[:n]
print(a)
print(b)