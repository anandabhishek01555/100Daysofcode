n=int(input())
l=[]
for i in range(1,n+1):
  if i%3==0:
    l.append("Clap")
  # i=str(i)
  elif("3" in str(i) or "6" in str(i) or "9" in str(i)):
    l.append("Clap")
  else:
    l.append(i)
print(l)