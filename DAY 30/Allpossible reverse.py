s="The sky is blue"
word=s.split()
word=list(reversed(word))
word=" ".join(word)
print(word)
print(' '.join(x[::-1] for x in s.split(" ")))
for a in s.split(" "):
    print(a[::-1],end=" ")
print()
word1=s.split()
word1=list(reversed(s))
word1="".join(word1)
print(word1)