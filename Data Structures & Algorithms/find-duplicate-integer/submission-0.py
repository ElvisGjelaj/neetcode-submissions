class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        prev_slow, prev_fast = nums[0], nums[nums[0]]

        while slow != fast:
            prev_slow, prev_fast = slow, fast
            slow, fast = nums[slow], nums[nums[fast]]
        
        return slow