a,b = map(int,input("Enter two numbers : ").split())
if(a>b):
    print(str(a)+" is greater than "+str(b))
elif(a<b):
    print(str(b)+" is greater than "+str(a))
else:
    print("Entered values are equal")