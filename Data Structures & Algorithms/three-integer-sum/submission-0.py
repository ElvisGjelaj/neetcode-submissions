class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triple = []
        for num in nums:
            target = -num
            left, right = 0, len(nums) -1 
            while left < right:
                if (nums[left] + nums[right] > target):
                    right -= 1
                elif (nums[left] + nums[right] < target):
                    left += 1
                elif ([num, nums[left], nums[right]] not in triples): 
                    triples.append([num, nums[left], nums[right]])
        return triples