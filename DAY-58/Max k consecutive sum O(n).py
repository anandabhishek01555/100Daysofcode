a=list(map(int(input().split())))
k=int(input())
s=0
x=0
s=sum(a[:k])
s1=s
for i in range(k,len(a)):
    s1=s1+a[i]
    s1=s1-a[x]
    x+=1
    if(s1>s):
        s=s1
print(s) 