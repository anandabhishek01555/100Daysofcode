def monkey(l):
  a=l
  b=[0]*len(l)
  c=0
  while(b!=l):
    c+=1
    b=[0]*len(l)
    for i in range(len(l)):
      b[l[i]-1] = a[i]
    a=b 
  return c      
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(monkey(l))        
        