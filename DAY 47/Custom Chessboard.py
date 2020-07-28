for _ in range(int(input())):
    n=input().split(maxsplit=1)
    x=int(n[0])
    for i in range(x):
        for j in range(x):
            if(n[1]=="W"):
                if((i+j)%2==0):
                    print("W",end="")
                else:
                    print("B",end="")
                # print()
            else:
                if((i+j)%2==0):
                    print("B",end="")
                else:
                    print("W",end="")
        print()
                
    









