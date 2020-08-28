def totalWays(n, m):
    if n < 0:
        return 0 
    if n == 0:
        return 1 
    count = 0
    for i in range(1, m + 1):
        count += totalWays(n - i, m) 
    return count 
n = int(input())
m = int(input()) 
print(f"Total ways to reach the {n}'th stair with at-most {m} steps are",
          totalWays(n, m))