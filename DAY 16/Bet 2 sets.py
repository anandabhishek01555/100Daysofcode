#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    c=0
    for i in range(max(a),min(b)+1):
        f=1
        for z in a:
            if(i%z!=0):
                f=0;
                break
        for z in b:
            if(z%i!=0):
                f=0
                break
        if(f==1):
            c+=1
    return c



    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    print(getTotalX(arr, brr))

