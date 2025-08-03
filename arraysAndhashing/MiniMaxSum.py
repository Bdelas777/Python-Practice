#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    suma = sum(arr)
    example = suma - max(arr)
    example2 = suma - min(arr)
    print("{:.0f} {:.0f}".format(example, example2)) 
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    