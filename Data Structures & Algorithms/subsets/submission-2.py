class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        def dfs(i):

            if i >= len(nums):
                res.append(subsets.copy())
                print(subsets)
                return
            
            # include nums[i]
            subsets.append(nums[i])
            dfs(i + 1)

            #exclude nums[i]
            subsets.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
