p,d,m,s=map(int,input().split())
games = 0
if(s<p):
    print("0")
else:
    while s >= 0:
        s -= p
        p = max(p - d, m)
        games += 1
        if(s-p<0):
            break
    print(games)
    