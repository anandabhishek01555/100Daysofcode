c=1
s=input()
for l in s:
    if l.isupper():
        c+=1
print(c)

# OR
print(sum(map(str.isupper,input()))+1)