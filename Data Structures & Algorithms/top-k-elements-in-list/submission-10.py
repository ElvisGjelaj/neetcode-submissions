from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = Counter(nums).most_common(k)
        res = []
        for n,f in num:
            res.append(n)
        return res
