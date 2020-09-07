n=int(input())
c=0
s=0
temp=n
while(n>0):
    r=n%10
    c+=1
    n=n//10
    n=temp
    while(n>0):
        r=n%10
        s+=r**c
        n=n//10
    if (s==temp):
        print("True")
    else:
        print("False")