from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # PASO 1: Contar frecuencias de cada carácter
        count = Counter(s)
        print(f"1. Conteo de caracteres: {dict(count)}")
        
        # PASO 2: Crear un max heap usando valores negativos
        # Python tiene min heap por default, así que usamos valores negativos
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        print(f"2. Max heap inicial: {maxHeap}")
        
        # PASO 3: Inicializar variables
        prev = None      # Guarda el carácter usado previamente
        res = ""         # Resultado final
        
        print("\n3. Proceso de construcción:")
        step = 1
        
        # PASO 4: Construir la cadena reorganizada
        while maxHeap or prev:
            print(f"   Paso {step}:")
            print(f"   - Heap: {maxHeap}")
            print(f"   - Prev: {prev}")
            print(f"   - Resultado actual: '{res}'")
            
            # Si no hay caracteres disponibles pero tenemos prev, es imposible
            if prev and not maxHeap:
                print("   ❌ No se puede reorganizar: no hay caracteres disponibles")
                return ""
            
            # Tomar el carácter más frecuente
            cnt, char = heapq.heappop(maxHeap)
            print(f"   - Carácter seleccionado: '{char}' (frecuencia: {-cnt})")
            
            # Agregarlo al resultado
            res += char
            cnt += 1  # Decrementar frecuencia (recordar que es negativo)
            print(f"   - Nueva frecuencia de '{char}': {-cnt}")
            
            # Si había un carácter previo, regresarlo al heap
            if prev:
                heapq.heappush(maxHeap, prev)
                print(f"   - Regresando al heap: {prev}")
                prev = None
            
            # Si el carácter actual aún tiene frecuencia > 0, guardarlo como prev
            if cnt != 0:  # cnt es negativo, así que != 0 significa que aún quedan
                prev = [cnt, char]
                print(f"   - Guardando como prev: {prev}")
            
            print(f"   - Resultado después del paso {step}: '{res}'")
            print()
            step += 1
        
        return res

# Ejemplo de uso
solution = Solution()

print("=" * 60)
print("EJEMPLO 1: s = 'bcaaa'")
print("=" * 60)
result1 = solution.reorganizeString("bcaaa")
print(f"Resultado final: '{result1}'")
