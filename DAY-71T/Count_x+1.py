#Find the max count of successive elements present in the givem list

a=list(map(int,input().split()))
a=sorted(a)
m=a[0]
c=1
for i in range(len(a)):
    if a[i]>m:
        m=a[i]
    if i<len(a)-1:
        if m+1==a[i+1]:
            c+=1
        else:
            c=1
print(c)