# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

n=int(input("Enter the elements in list : "))
l=input().split()
c=0
for x in l:
    if len(x)>1 and x[0]==x[-1]:
        c+=1
print("The count is : ",c)