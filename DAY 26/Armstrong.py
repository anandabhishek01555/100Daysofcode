s=0
n=int(input())
temp=n
while n!=0:
    r=n%10
    s+=r**3
    n=n//10
if(temp==s):
    print("Yes")
else:
    print("No")
