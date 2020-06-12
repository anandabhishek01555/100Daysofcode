n=int(input())
l=[int(l) for l in input().split()]
k=[None]*len(l)
visited=-1
for i in range(0,len(l)):
    c=1
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            c+=1
            k[j]=visited
    if(k[i]!=visited):
        k[i]=c

print(len(l)-max(k))