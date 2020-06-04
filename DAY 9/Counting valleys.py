n=int(input())
s=input()
stream=0
count=0
prev_stream=0
for i in range(0,n):
    if(s[i]=="U"):
        stream+=1
    elif(s[i]=="D"):
        stream-=1
    if(stream==0 and prev_stream<0):
        count+=1
    prev_stream = stream
print(count)
