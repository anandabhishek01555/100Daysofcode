# A Program to check if we have a consectutive elements that sums up to 0.


def subArrayExists(arr,n): 
    n_sum = 0
    s = set() 
  
    for i in range(n): 
        n_sum += arr[i] 
        if n_sum == 0 or n_sum in s: 
            return True
        s.add(n_sum) 
    return False
  
arr = list(map(int,input().split()))    
n = len(arr) 
if subArrayExists(arr, n) == True: 
    print("Yes") 
else: 
    print("No") 