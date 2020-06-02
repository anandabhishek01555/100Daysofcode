
spam=["cat","bat","dog"]

def string(param,n):
    spam.append(n)
    i=",".join(map(str, param))
    j=i.rfind(",")
    return i[:j] + "," + i[j+1:]

print(string(spam,"and"))