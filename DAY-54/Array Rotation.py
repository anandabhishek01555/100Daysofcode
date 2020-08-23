k=int(input())
a=list(map(int,input().split()))
x=a[len(a)-k:]
x.extend(a[:len(a)-k])
print("Right rotation :",x)
x=a[k:]
x.extend(a[:k])
print("Left rotation :",x)