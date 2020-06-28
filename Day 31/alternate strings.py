a = "Abhishek"
len1 = len(a)
b = "12345678910"
len2 = len(b)
result = ""
c=min(len(a),len(b))
for i in range(c):
    result += a[i]
    result += b[i]
if(len(a)>len(b)):
    for i in range(c,len(a)):
        result+=a[i]
    print(result)
else:
    for i in range(c,len(b)):
        result+=b[i]
    print(result)
    