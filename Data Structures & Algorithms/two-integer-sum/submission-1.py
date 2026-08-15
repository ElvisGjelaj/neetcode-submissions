class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in len(nums):
            for j in len(nums):
                if i + j == target:
                    retunr [i, j]