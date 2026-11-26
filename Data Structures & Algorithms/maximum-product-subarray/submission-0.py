class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = res = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            candidates = (n, cur_max * n, cur_min * n)
            cur_max = max(candidates)
            cur_min = min(candidates)
            res = max(res, cur_max)

        return res