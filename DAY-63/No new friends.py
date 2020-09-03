f=[[j for j in range(input())]for i in range(input())]
n=18
x=[]
# print(len(f))
for i in range(len(f)):
    for j in range(2):
        x.append(f[i][j])
x=set(x)
if (len(x)==n):
    print("True")
else:
    print("False")