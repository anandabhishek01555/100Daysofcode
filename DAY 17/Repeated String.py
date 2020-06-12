s=input()
c=0
n=int(input())
t=0
t=s.count('a')
t*=n//len(s)
t+=s[0:n%len(s)].count('a')
print(t)
    