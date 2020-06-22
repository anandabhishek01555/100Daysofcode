import re
def happy(n, b):
    if b.count("_") == 0 and len(re.sub(r'((.)\2+)', "", b)) != 0:
        return "NO"
    for a in set(b):
        if a != "_" and b.count(a) == 1:
            return "NO"
    return "YES"
for _ in range(int(input())):
    n = int(input())
    b = input()
    print(happy(n, b))