# Find the no. of counts needed so that each element in the list reaches the maximum
# element present.

a=list(map(int,input().split()))
a=sorted(a)
x=a.index(min(a))
m=max(a[x:len(a)])
print(m-a[x])