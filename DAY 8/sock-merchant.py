n=int(input())
l=[int(l) for l in input().split()]
k=[None]*len(l)
visited=-1
s=0
for i in range(0,len(l)):
    c=1
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            c+=1
            k[j]=visited
    if(k[i]!=visited):
        k[i]=c

  
for i in range(0, len(k)):    
    if(k[i] != visited):
        x=k[i]//2
        s+=x
        # print(str(k[i]),end=" ");
print(s)
