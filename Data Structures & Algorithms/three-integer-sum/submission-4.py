class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triples = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) -1 
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if (total >0):
                    right -= 1
                elif (total < 0):
                    left += 1
                elif (total == 0): 
                    triples.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left +=1
        return triples