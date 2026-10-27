class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_cons = 0

        for num in nums:
            curr_longest_cons = 1
            curr_num = num
            if num - 1 not in nums_set:
                while curr_num + 1 in nums_set:
                    curr_longest_cons += 1
                    curr_num += 1

            longest_cons = max(longest_cons, curr_longest_cons)

        return longest_cons
