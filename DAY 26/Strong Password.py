n=int(input())
s=input()
c=0
if any(i.isupper() for i in s) == False:
    c+=1
if any(i.islower() for i in s) == False:
    c+=1
if any(i.isdigit() for i in s) == False:
    c+=1
if any(i in '!@#$%^&*()-+' for i in s)==False:
    c+=1
print(max(c,6-n))

    