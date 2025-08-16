#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    def es_palindromo(cadena, izq, der):
        """Verifica si la subcadena desde izq hasta der es palíndromo"""
        while izq < der:
            if cadena[izq] != cadena[der]:
                return False
            izq += 1
            der -= 1
        return True
    
    izq = 0
    der = len(s) - 1
    
    # Comparar desde los extremos hacia el centro
    while izq < der:
        if s[izq] != s[der]:
            # Encontramos una diferencia
            # Opción 1: eliminar el carácter de la izquierda
            if es_palindromo(s, izq + 1, der):
                return izq
            # Opción 2: eliminar el carácter de la derecha
            elif es_palindromo(s, izq, der - 1):
                return der
            else:
                # No se puede formar palíndromo eliminando un carácter
                return -1
        
        izq += 1
        der -= 1
    
    # Si llegamos aquí, la cadena ya es un palíndromo
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()