def makingAnagrams(s1, s2):
    s3=list(s2)
    for i in s1:
        if i in s3:
            print(i)
            s3.remove(i)
    no_common=len(s2)-len(s3)
    return len(s1)+len(s2)-2*no_common
print(makingAnagrams(input(), input()))