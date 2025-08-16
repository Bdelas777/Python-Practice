#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    
    positivos = len([x for x in arr if x > 0])
    negativos = len([x for x in arr if x < 0])
    ceros = len([x for x in arr if x == 0])
    
    print("{:.6f}".format(positivos/n))
    print("{:.6f}".format(negativos/n))
    print("{:.6f}".format(ceros/n))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
