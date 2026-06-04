class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        champ_num = -1
        champ_occurances = 0
        elem_dict = {}
        for num in nums:
            try:
                elem_dict[num] += 1
            except:
                elem_dict[num] = 1
            if elem_dict[num] > champ_occurances:
                champ = num
                champ_occurances = elem_dict[num]
        return champ