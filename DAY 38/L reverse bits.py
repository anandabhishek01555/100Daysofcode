def num1(num):
    res = [int(x) for x in str(num)] 
    rev=res[::-1]
    a=""
    for i in rev:
        a+=str(i)
    return int(a)
        
n=int(input())
print(num1(n))


