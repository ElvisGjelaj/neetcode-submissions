class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        
        for num in nums:
            if num in num_freq.keys():
                num_freq[num] += 1
            else:
                num_freq[num] = 1
        
        all_nums = list(num_freq.keys())
        all_nums.sort(key=lambda x: num_freq[x], reverse=True)
        return all_nums[:k]
