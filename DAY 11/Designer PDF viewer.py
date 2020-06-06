l=[int(l) for l in input().split()]
word=[l[ord(c)-ord("a")] for c in input()]
print(max(word)*len(word))