class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        champ = -1
        elem_dict = {}
        for num in nums:
            try:
                elem_dict[num] += 1
            except:
                elem_dict[num] = 1
            if elem_dict[num] > champ:
                champ = num