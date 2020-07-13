n=int(input())
while(n>0):
    l=input()
    e=""
    for i in range(len(l)):
        if i+1 < (len(l)):
            if(l[i]!=l[i+1]):
                e+=l[i]
    x=(len(l))-1
    e+=l[x]
    c=len(l)-len(e)
    print(c)
    n-=1