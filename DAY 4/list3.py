#Program to check presence of an input taken by user

myPets = ['Zophie', 'Pooka', 'Fat-tail'] 
print('Enter a pet name:') 
name = input() 
if name in myPets:    
    print(name) 
else:    
    print(name + ' is not my pet.')