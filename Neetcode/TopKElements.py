class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        sortedFreq = sorted(freq.items(), key=lambda item: item[1],reverse= True)
        lista = []
        for i in range(k):
            lista.append(sortedFreq[i][0])
        return lista
        
        
        
       