l=list(map(int,input().split()))
m=[]
n=[]
for i in range(len(l)):
    if l[i] not in m:
        m.append(l[i])
        n.append(l.count(l[i]))
for i in range(len(n)):
    print(m[i],"-->",n[i])