n,k=map(int,input().split())
c=[int(c) for c in input().split()]
energy = 100 #initial energy
i = k % n #initial jump from 0
energy -= c[i] * 2 + 1 #initial energy loss
while i != 0:
    i = (i + k) % n
    energy -= c[i] * 2 + 1
print(energy)