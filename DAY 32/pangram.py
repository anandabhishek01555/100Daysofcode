s=input()
x="abcdefghijklmnopqrstuvwxyz"
c=0
a=s.lower()
for i in x:
    if i in a:
        c+=1
if c==26:
    print("pangram")
else:
    print("not pangram")