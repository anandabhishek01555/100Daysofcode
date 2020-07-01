a=int(input())
while a>0:
    n=input()
    if n[0] == n:
        print('NO')
    for i in range(1,len(n)):
        x=[]
        x.append(n[:i])
        
        while(len(''.join(x)) < len(n)):
            x.append(str(int(x[-1])+1))
        if ''.join(x)==n:
            print('YES',x[0])
            break
        if i == len(n) - 1:
            print('NO')
    a-=1