x1=int(input())
x2=int(input())
a=(bin(x1)[2:])
b=(bin(x2)[2:])
z="0"
c=0
z1=max(len(a),len(b))-min(len(a),len(b))
if(len(a)<len(b)):
    n1=z*z1 + a
    n2=b
else:
    n1=z*z1 + b
    n2=a
print(n1)
print(n2)
for i in range(len(n1)):
    if(n1[i]!=n2[i]):
        c+=1
print(c)