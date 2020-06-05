n=int(input())
k=[]
for i in range(0,n):
    x,y,z=map(int,input().split())
    if(abs(z-x)==abs(z-y)):
        k.append("Mouse C")
    elif(abs(z-x)<abs(z-y)):
        k.append("Cat A")
    else:
        k.append("Cat B")
for i in range(0,n):
    print(k[i])