for _ in range(int(input())):
    n=int(input())
    if n<=1:
        print('You cannot generate christmas tree')
    elif n>20:
        print('Tree is no more')
    else:
        for i in range(1,n+2):
            for j in range(n-i+1):
                print(' ',end='')
            for j in range(1,2*i):
                print('*',end='')
            print()
 
        o=1
        x=n
        for k in range(2,x):
            for i in range(1,n):
                for j in range(o):
                    print(' ',end='')
                for j in range(n-i-1):
                    print(' ',end='')
                for j in range(1,2*i+2):
                    print('*',end='')
                print()
            o+=1
            n-=1
        for i in range(2):
            for j in range(x):
                print(' ',end='')
            print('*')




