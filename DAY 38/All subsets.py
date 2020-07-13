def sub_lists(list1): 
    sets = [[]]
    for i in range(len(list1)):
        length = len(sets)
        for j in range(length):
            sets.append(sets[j] + [list1[i]])
    return sets
l1 = [int(l1) for l1 in input().split()] 
print(sub_lists(l1)) 