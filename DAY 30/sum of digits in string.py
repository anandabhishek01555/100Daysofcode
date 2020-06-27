s="12abhi1a3"
k=[]
e=""
sum=0
for i in s:
    if(i.isdigit()):
        e+=i
    else:
        if(e!=""):
            k.append(e)
            e=""
k.append(e)
for i in k:
    if(i.isdigit()==False):
        k.remove(i)
    sum+=int(i)
print(sum)