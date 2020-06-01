# Write a Python program to generate all permutations of a list in Python.

import itertools
l=[1,2,3,4]
k=list(itertools.permutations(l))
print(k)