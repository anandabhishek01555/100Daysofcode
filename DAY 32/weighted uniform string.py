s=input()
u=set()
pc=w=0
for i in s:
    c=ord(i)-96
    if pc==c:
        w+=c
    else:
        pc=w=c
    u.add(w)
print(u)
n=int(input())
while(n>0):
    if int(input()) in u:
        print("Yes")
    else:
        print("No")
    n-=1