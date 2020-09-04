# Min Sum array
a=list(map(int,input().split()))
s=0
temp=a[0]+a[1]
for i in range(len(a)-1):
    # print(i)
    s=a[i]+a[i+1]
    if(s<temp):
        temp=s
print(temp)
 