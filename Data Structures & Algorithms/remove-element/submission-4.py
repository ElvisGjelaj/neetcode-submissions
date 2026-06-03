class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for idx, num in enumerate(nums):
            if nums[idx] != val:
                nums[k] = nums[idx]
                k += 1
        return k
