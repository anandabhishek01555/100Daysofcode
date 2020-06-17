def serviceLane(n, cases):
    return [min(width[x:y+1]) for x,y in cases]

n,t=map(int,input().split())
width = list(map(int, input().rstrip().split()))
cases = []
for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))
print(serviceLane(n, cases))