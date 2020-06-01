# Write a Python program to find the list of words that are longer than n from a given list of words.

l=["Abhishek","John","David","Tom","Abhi"]
n=int(input())
k=[]
for i in l:
    if(len(i)>n):
        k.append(i)
print(k)