#This program will take your name as input and print Hello Yourname and print the no. of characters in your name.
#eg. Hello Abhishek

print("Enter your name please : ",end="") #end="" for printing without linechange
name=input()
print("Hello "+ name)
print("Your name has " + str(len(name)) + " chracters" ) #str(len(name)) as concatenation can be done with same datatype

