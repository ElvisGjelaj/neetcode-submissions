class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxList = []
        l = 0
        for r in range(k, len(nums)):
            window = nums[l:r]
            maxList.append(max(window))
            l += 1
        return maxList