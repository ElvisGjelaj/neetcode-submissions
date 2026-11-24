class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        
        for m in nums:
            prev2, prev1 = prev1, max(prev1, m + prev2)
        
        return prev1
