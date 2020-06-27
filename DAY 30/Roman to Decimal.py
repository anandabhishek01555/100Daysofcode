
def romanToInt(rom): 
    value = { 
        'M': 1000, 
        'D': 500, 
        'C': 100, 
        'L': 50, 
        'X': 10, 
        'V': 5, 
        'I': 1
    } 
    p = 0
    ans = 0
    n = len(rom)  
    for i in range(n-1, -1, -1):  
        if value[rom[i]] >= p: 
            ans += value[rom[i]] 
  
        # If smaller than previous   
        else: 
            ans -= value[rom[i]] 
  
        # Update previous 
        p = value[rom[i]] 
  
    print(ans) 
n=input()
romanToInt(n) 