n=int(input())
x="hackerrank"
while(n!=0):
    j=0
    s=input()
    if(len(s)<len(x)):
        print("No")
    else:
        for i in range(len(s)):
            if(j<len(x) and s[i]==x[j]):
                j+=1
        if(j==len(x)):
            print("YES")
        else:
            print("NO")
    n-=1
    j=0