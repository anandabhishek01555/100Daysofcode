s="123#avbc#456#ejkn#789"
x=0
for i in s:
    if(i=="#"):
        if(x==0):
            x=1
        else:
            x=0
    else:
        if(x==0):
            print(i,end="")
