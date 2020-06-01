# Write a Python function that takes two lists and returns True if they have at least one common member.

l=[1,2,3,4,5]
k=[4,5,6,7,8]
c=0
for i in k:
    if i in l:
        c+=1

if(c==0):
    print("False")
else:
    print("True")
