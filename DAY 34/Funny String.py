n=int(input())
while(n>0):
    m=[]
    c=0
    s=input()
    sr=s[::-1]
    for i in range(len(s)):
        if i+1 < len(s):
            x=abs(ord(s[i+1])-ord(s[i]))
            m.append(x)
    for i in range(len(sr)):
        if i+1 < len(sr):
            j=abs(ord(sr[i+1])-ord(sr[i]))
            if j == m[i]:
                c+=1
    if c==len(m):
        print("Yes")
    else:
        print("No")
    n-=1
