class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            if l == r -1:
                return -1
            idx = (r + l) // 2
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                r = idx
            elif nums[idx] < target:
                l = idx
        return -1