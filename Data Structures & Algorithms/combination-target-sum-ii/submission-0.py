class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, total):

            if total == target:
                res.append(subset.copy())
                return

            if i >= len(candidates) or total > target:
                return

            #include candidates[i]
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            #dont include candidates[i]
            j = i
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1

            subset.pop()
            dfs(j, total)
        
        dfs(0,0)

        return res
            
