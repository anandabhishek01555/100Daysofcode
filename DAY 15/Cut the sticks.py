#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the cutTheSticks function below.

def cutTheSticks(arr):

    l = len(arr) ; c = Counter(arr)
    for k in sorted(c) : 
        yield l 
        l -= c[k]

    m=[]
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(cutTheSticks(arr))

