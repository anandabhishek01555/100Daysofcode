x,y,z=map(int,input().split())
c=0
for i in range(x,y+1):
    i=str(i)
    k = int(i[::-1])
    i=int(i)
    a=i-k
    b=a%z
    if(b==0):
        c+=1
print(c)
