from itertools import combinations

# Complete the alternate function below.
def alternate(s):
    results=[]
    st=list(set(s))
    print(st)
    if len(s)<2:
        return 0
    else:
        combos=list(combinations(st,len(st)-2))
        print(combos)
        for i in combos:
            vals=[]
            temp=s
            for x in i:
                temp=temp.replace(x,"")
            print(temp)    
            for y in range(len(temp)-1):
                if temp[y]==temp[y+1]:
                    vals.append(False)
                else:
                    vals.append(True)
            if all(vals)==True:
                results.append(len(temp))
            else:
                results.append(0)

    return max(results)


l = int(input())
s = input()
print(alternate(s))

