class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            curr_longest = 1
            while (num + 1):
                curr_longest += 1
            if longest < curr_longest:
                longest = curr_longest
        return longest
