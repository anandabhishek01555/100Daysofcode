n,m=map(int,input().split())
a=[int(a) for a in input().split()]
b=[int(b) for b in input().split()]
c=0
for x in range(max(a),min(b)+1):
    f=1
    for z in a:
        if(x%z!=0):
            f=0
            break
    for z in b:
        if(z%x!=0):
            f=0
            break
    if(f==1):
        c+=1
print(c)
