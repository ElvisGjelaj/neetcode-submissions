class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subsets = []

        def dfs(i, total):

            if total == target:
                res.append(subsets.copy())
                return

            if i >= len(nums) or total > target:
                return

            # include nums[i]
            subsets.append(nums[i])
            dfs(i, total + nums[i])
            
            # don't include nums[i]
            subsets.pop()
            dfs(i + 1, total)

        dfs(0, 0)

        return res

                      
            
        