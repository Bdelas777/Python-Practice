class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  # Ordenamos por el segundo valor
        current_end = float('-inf')
        length = 0
        for a,b in pairs:
            if a > current_end:
                current_end  = b
                length +=1
        return length
