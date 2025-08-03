#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_matrixAY matrix as parameter.
#

def flippingMatrix(matrix):
    """
    Encuentra la suma máxima posible del cuadrante superior izquierdo
    después de voltear filas y/o columnas de la matriz.
    
    Para cada posición (i,j) en el cuadrante superior izquierdo,
    podemos elegir el máximo de 4 valores posibles:
    - matrix[i][j] (sin voltear)
    - matrix[i][2n-1-j] (voltear fila i)
    - matrix[2n-1-i][j] (voltear columna j)  
    - matrix[2n-1-i][2n-1-j] (voltear ambos)
    """
    
    # n es el tamaño del cuadrante que queremos maximizar
    size = len(matrix)
    n = size // 2
    
    max_sum = 0
    
    # Para cada posición en el cuadrante superior izquierdo
    for i in range(n):
        for j in range(n):
            # Los 4 valores posibles que pueden terminar en la posición (i,j)
            # después de voltear filas y/o columnas
            option1 = matrix[i][j]                    # Sin voltear
            option2 = matrix[i][size-1-j]             # Voltear columna j
            option3 = matrix[size-1-i][j]             # Voltear fila i
            option4 = matrix[size-1-i][size-1-j]      # Voltear ambos
            
            # Elegimos el máximo de las 4 opciones
            max_value = max(option1, option2, option3, option4)
            max_sum += max_value
    
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
