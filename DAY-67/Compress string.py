s=input()
x=""
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        x+=s[i]
x+=s[-1]
print(x)