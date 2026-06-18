class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            curr_longest = 1
            if (num - 1) not in num_set:
                while (num + curr_longest) in num_set:
                    curr_longest += 1
                longest = max(longest, curr_longest)
        return longest
