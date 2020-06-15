n=int(input())
a=list(map(int,input().strip().split()))
k=[]
flag=0
for i in range(n):
    for j in range(i+1,n):
        if(a[i]==a[j]):
            x=j-i
            flag+=1
            k.append(x)
if(flag==0):
    print(-1)
else:
    print(min(k))

            
    