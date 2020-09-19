s=input()
words=[i for i in input().split()] 
l=[]
for i in range(len(words)):
    if words[i][0:len(s)]==s:
        l.append(words[i])
print(l)