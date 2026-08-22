class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        nums.sort()
        def dfs(i):

            if i >= len(nums):
                res.append(subsets.copy())
                return 
            
            #include nums[i]
            subsets.append(nums[i])
            dfs(i + 1)

            #dont include nums[i]
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            subsets.pop()
            dfs(j)

        dfs(0)
        return res