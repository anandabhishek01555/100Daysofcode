bday={"Mohan":"10 Dec" , "Rohan":"13 Dec" , "Sohan": "19 Oct" , "Abhi" : "12 Dec"}
while True:
    n=input("Enter a name : ")
    if n in bday:
        print(n + " has birthday on " + bday[n])
        check=input("You want to check other's detail [y/n] : ")
        if(check=="n"):
            break
        else:
            continue

    else:
        print("Record not found .")
        b=input("Enter the record : ")
        bday[n]=b
        print("Value Updated .")

print(bday)