# 1387. Sort Integers by The Power Value

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def asignar(value):
            paso = 0 
            while value != 1:
                if value % 2 == 0:
                    value /= 2 
                    paso+=1
                else:
                    value = 3 * value + 1
                    paso+=1
            return paso

        dicts = {}
        for i in range(lo,hi+1):
            pasos = asignar(i)
            dicts[i] =  pasos 
        
        ordenado_lista = sorted(dicts.items(), key=lambda item: item[1])

        return ordenado_lista[k-1][0]