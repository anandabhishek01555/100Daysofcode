p,q=map(int,input().split())
found=False
if(p<9):
    p=9
    print('1')
for i in range(p,q+1):
    n=i**2
    n=str(n)
    d=len(n)//2
    n1=n[:d]
    n2=n[d:]
    if i == (int(n1)+int(n2)):
        print(i)
        found=True
if(not found):
    print("INVALID RANGE")
    
