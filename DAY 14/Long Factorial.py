def extraLongFactorials(n):
    if n>=1:
        return n*extraLongFactorials(n-1)
    else:
        return 1
n = int(input())
extraLongFactorials(n)