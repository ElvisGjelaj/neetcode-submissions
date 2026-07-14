class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            
            #left side
            if nums[l] <= nums[m]:
                if nums[l] > target or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            #right side
            else:
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
        return -1

