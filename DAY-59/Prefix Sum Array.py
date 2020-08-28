# Consider an array of size N with all initial values as 0. Perform given 'm' add operations from index 'a' to 'b' and evaluate highest element in array. 
# An add operation adds 100 to all elements from index a to b (both inclusive)

N=int(input())
m=int(input())
k=[0]*N
print(k)
while(m>0):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        k[i-1]+=100
    m-=1
print(max(k))