n=int(input())
l=[int(l) for l in input().split()]
m=[int(m) for m in input().split()]
k=[]
for i in range (len(l)):
    x=m[i]//l[i]
    k.append(x)
print(min(k))