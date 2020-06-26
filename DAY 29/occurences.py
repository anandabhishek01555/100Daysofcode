def superReducedString(s):
    res = [] # stack
    for c in s:
        if res and res[-1] == c: # peek what's on top
            res.pop()
        else:
            res.append(c)
    res = ''.join(res)
    return res or 'Empty String'

s = "baab"
print(superReducedString(s))