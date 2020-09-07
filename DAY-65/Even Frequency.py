a=list(map(int,input().split()))
res=0
for i in range(len(a)):
    res = res ^ i
    if len(a)%2!=0:
        print("Not Even Frequency")
        break
    if res==0:
        print("Even Frequency")
        break
    else:
        print("Not Even Frequency")
        break
