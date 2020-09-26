#Check if two strings are anagrams of each other or not.

s0=input()
s1=input()
c=0
if len(s0)==len(s1):
  for i in range(len(s0)):
    if s0[i] in s1:
      c+=1
  if c==len(s0):
    print("True")
else:
  print("False")