l=[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,11,1,1]
m=[]
k=[]
for i in l:
    if i not in k:
        k.append(i)
        if i in k:
            x=l.count(i)
            m.append(x)
print(m)
    