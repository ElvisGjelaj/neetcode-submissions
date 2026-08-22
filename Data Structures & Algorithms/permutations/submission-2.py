class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(choices):
            
            if not choices:
                res.append(subset.copy())
                return
            
            for idx, choice in enumerate(choices):
                subset.append(choice)
                dfs(choices[0:idx] + choices[idx + 1:])
                subset.pop()
            
        dfs(nums)
        return res
