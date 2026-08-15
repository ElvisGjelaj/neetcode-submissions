class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elem_freq = {}
        
        for num in nums:
            try: 
                elem_freq[num] += 1
            except:
                elem_freq[num] = 1
        
        k_nums = list(elem_freq.keys())[:k]
        least_key = min(k_nums)
        for key_num in k_nums[k:]:
            if key_num > least_key: 
                idx = k_nums.index(least_key)
                k_nums[idx] = key_num
        
        return k_num
