def theLoveLetterMystery(s):
    tot = 0
    for i,j in enumerate(range(len(s)//2),1):
        a = s[ j]
        b = s[-i]
        tot+= abs(ord(a)-ord(b))
    return tot

for _ in range(int(input())):
    print(theLoveLetterMystery(input()))