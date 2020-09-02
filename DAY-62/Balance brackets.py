b=input()
bal=0
ans=0
for i in range(len(b)):
    if b[i]=="(":
        bal+=1
    else:
        ans+=1
print(abs(bal-ans))
    