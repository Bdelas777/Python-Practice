#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Extraer AM/PM (ultimos 2 caracteres)
    period = s[-2:]
    
    # Extraer la hora sin AM/PM (todos excepto ultimos 2)
    time_part = s[:-2]
    
    # Separar horas, minutos y segundos
    hours, minutes, seconds = time_part.split(':')
    hours = int(hours)
    
    if period == 'AM':
        # Para AM: si es 12, cambiar a 00; sino mantener igual
        if hours == 12:
            hours = 0
    else:  # PM
        # Para PM: si NO es 12, sumar 12; si es 12 mantener igual
        if hours != 12:
            hours += 12
    
    # Formatear con 2 digitos para las horas
    return "{:02d}:{}:{}".format(hours, minutes, seconds)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
