class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_line(houses):
            prev2, prev1 = 0, 0
            for money in houses:
                prev2, prev1 = prev1, max(money + prev2, prev1)
            return prev1
        
        if len(nums) == 1:
            return nums[0]

        return max(rob_line(nums[1:]), rob_line(nums[:-1]))
