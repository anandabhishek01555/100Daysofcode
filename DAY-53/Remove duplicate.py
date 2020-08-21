def remove_duplicate(n, arr):
    m=[]
    for i in range(n):
        m.append(arr[i])
    
    arr.clear()
    for i in m:
        if i not in arr:
            arr.append(i)
    return(len(arr))
    
#  Driver Code Starts
#Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        n = remove_duplicate(n, arr)
        for i in range(n):
            print (arr[i], end=" ")
        print()


# } Driver Code Ends