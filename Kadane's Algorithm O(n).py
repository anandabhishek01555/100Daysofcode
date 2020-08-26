def maxSubArraySum(a,size): 
    s =a[0] 
    s1 = a[0] 
      
    for i in range(1,size):
        # print(a[i], s1 + a[i])
        s1 = max(a[i], s1 + a[i]) 
        s = max(s,s1) 
    return s 

a = list(map(int,input().split()))
print("Maximum contiguous sum is" , maxSubArraySum(a,len(a))) 