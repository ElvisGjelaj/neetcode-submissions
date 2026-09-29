import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 1) + 1
        
        keys = list(freq.keys())
        keys.sort(key=lambda x: freq[x], reverse=True)
        return keys[:k]
        



