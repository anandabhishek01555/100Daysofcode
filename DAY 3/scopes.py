def spam():
    eggs = 9
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    
spam()

# Output will be 9, since it is locally stored for spam()

def spam(): 
    global eggs
    eggs = '10'
    
eggs = '20' 
spam() 
print(eggs)
