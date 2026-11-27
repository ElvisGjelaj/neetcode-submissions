class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        sums = {0}
        for num in nums:
            new_sums = set()
            for s in sums:
                new_sums.add(s)          # skip num
                new_sums.add(s + num)    # take num
            sums = new_sums
            if target in sums:
                return True

        return False