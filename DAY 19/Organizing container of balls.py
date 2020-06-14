n=int(input())
container = []
for _ in range(n):
    container.append(list(map(int, input().rstrip().split())))

mr=[]
mc=[]
for i in range(0,len(container)):
    mr.append(sum(container[i]))
    j=0
    tot=0
    for j in range(0,len(container)):
        tot+=container[j][i]
    mc.append(tot)
mr.sort()
mc.sort()
if mr==mc:
    print("possible")
else:
    print("Impossible")