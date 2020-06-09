

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if k >= len(s) + len(t) : return "Yes"

    i = 0 ; m = min( len(s), len(t) )
    while i < m and s[i] == t[i] : 
        i += 1    
    d = len(s)-i + len(t)-i
        
    if k < d : 
        return "No"
    if k == d : 
        return "Yes"
    return "No" if (k-d)%2 else "Yes"   

s = input()
t = input()
k = int(input())
print(appendAndDelete(s, t, k))