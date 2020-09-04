nums=list(map(int,input().split()))
c=0
d=0
l=[]
for i in range(len(nums)):
    d=0
    n=nums[i]
    while(n>0):
        r=n%10
        d+=1
        n=n//10
    l.append(d)
for i in range(len(l)):
    if(l[i]%2!=0):
        c+=1
print(c)