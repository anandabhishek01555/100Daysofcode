# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

l=[1,2,3,4,5,6,7,8]
k=[]
for i in range(0,len(l)):
    if i==0 or i==4 or i==5 :
        l.pop(i)
print(l)
