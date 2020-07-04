s=[set(input()) for _ in range (int(input()))]
c=set.intersection(*s)
print(len(c))