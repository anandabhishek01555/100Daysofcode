s=input()
l=len(s)//3
k="SOS"*l
c=0
for i in range(len(s)):
    if(s[i]!=k[i]):
        c+=1
print(c)