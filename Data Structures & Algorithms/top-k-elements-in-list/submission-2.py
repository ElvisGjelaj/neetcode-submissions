class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elem_freq = {}
        
        for num in nums:
            try: 
                elem_freq[num] += 1
            except:
                elem_freq[num] = 1
        
        all_nums = list(elem_freq.keys())
        all_nums.sort(key=lambda x: elem_freq[x], reverse=True)
        return all_nums[:k]
