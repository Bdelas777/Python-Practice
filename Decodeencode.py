from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Codifica una lista de strings en un solo string.
        Formato: longitud#string para cada elemento
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        """
        Decodifica el string codificado de vuelta a una lista de strings
        """
        res = []
        i = 0
        while i < len(s):
            # Encontrar el '#' para obtener la longitud
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # Longitud del string
            i = j + 1  # Saltar el '#'
            j = i + length  # Posición final del string actual
            res.append(s[i:j])  # Extraer el string
            i = j  # Moverse al siguiente
        return res

# Ejemplos de uso
if __name__ == "__main__":
    solution = Solution()
    
    # Ejemplo 1: Lista simple
    print("=== Ejemplo 1 ===")
    lista1 = ["hola", "mundo", "python"]
    codificado1 = solution.encode(lista1)
    decodificado1 = solution.decode(codificado1)
    
    print(f"Original: {lista1}")
    print(f"Codificado: '{codificado1}'")
    print(f"Decodificado: {decodificado1}")
    print(f"¿Son iguales? {lista1 == decodificado1}")
    print()
    
    # Ejemplo 2: Con strings vacíos y especiales
    print("=== Ejemplo 2 ===")
    lista2 = ["", "a", "##", "hola#mundo"]
    codificado2 = solution.encode(lista2)
    decodificado2 = solution.decode(codificado2)
    
    print(f"Original: {lista2}")
    print(f"Codificado: '{codificado2}'")
    print(f"Decodificado: {decodificado2}")
    print(f"¿Son iguales? {lista2 == decodificado2}")
    print()
    
    # Ejemplo 3: Con espacios y caracteres especiales
    print("=== Ejemplo 3 ===")
    lista3 = ["uno dos", "tres", "", "cuatro#cinco"]
    codificado3 = solution.encode(lista3)
    decodificado3 = solution.decode(codificado3)
    
    print(f"Original: {lista3}")
    print(f"Codificado: '{codificado3}'")
    print(f"Decodificado: {decodificado3}")
    print(f"¿Son iguales? {lista3 == decodificado3}")
    print()
    
    # Ejemplo 4: Paso a paso del proceso
    print("=== Ejemplo 4: Proceso paso a paso ===")
    lista4 = ["abc", "de", "f"]
    print(f"Lista original: {lista4}")
    print("\nProceso de codificación:")
    result = ""
    for i, s in enumerate(lista4):
        encoded_part = str(len(s)) + "#" + s
        result += encoded_part
        print(f"  String '{s}' (longitud {len(s)}) -> '{encoded_part}'")
    
    print(f"\nResultado final codificado: '{result}'")
    
    print(f"\nProceso de decodificación de '{result}':")
    decoded = []
    i = 0
    step = 1
    while i < len(result):
        # Encontrar longitud
        j = i
        while result[j] != '#':
            j += 1
        length = int(result[i:j])
        print(f"  Paso {step}: Longitud encontrada = {length}")
        
        # Extraer string
        i = j + 1
        j = i + length
        extracted = result[i:j]
        decoded.append(extracted)
        print(f"  Paso {step}: String extraído = '{extracted}'")
        
        i = j
        step += 1
    
    print(f"\nResultado decodificado: {decoded}")