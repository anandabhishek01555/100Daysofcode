s1=input()
s2=input()
for i in range(len(s1)):
    if (s1[i] not in s2):
        print(s1[i],end="")
print()
for i in range(len(s2)):
    if (s2[i] not in s1):
        print(s2[i],end="")
print()
x=""
l1=len(s1)
l2=len(s2)
if l1>l2:
    for i in range(l1):
        if s1[i] in s2:
            x+=s1[i]
else:
    for i in range(l2):
        if s2[i] in s1 and s2[i] not in x:
            x+=s2[i]
print(x)