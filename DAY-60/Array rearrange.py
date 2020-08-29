def arrange(a,n):
    for i in range(len(a)):
        a[i]+=(a[a[i]]%n)*n
    for i in range(n):
        a[i]=int(a[i]/n)
    return (len(a))
a=list(map(int,input().split()))
arrange(a,len(a))
for i in a:
    print(i,end=" ")
print()


# def sol(a):
#     l=[]
#     for i in range(len(a)):
#         l.append(a[i])
#     a.clear()
#     for i in range(len(l)):
#         a.append(l[l[i]])
#     return len(a)