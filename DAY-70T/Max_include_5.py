# Find the greatest possible number formed by including one more digit as 5 in the given number.


n=int(input())
l=[]
if n>0:
  n=str(n)
  l.append(n[0])
  for i in range(1,len(n)+1):
    if i==1:
      l.append("5")
    else:
      l.append(n[i-1])
  for i in l:
    print(i,end="")
  print()
else:
  n=str(n)
  for i in n:
    l.append(i)
  l.append("5")
  for i in l:
    print(i,end="")
  print()