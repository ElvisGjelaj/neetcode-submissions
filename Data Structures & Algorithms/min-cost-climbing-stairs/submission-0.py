class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}

        def dp(i):
            if i == 0 or i == 1:
                return cost[i]
            
            if i in mem:
                return mem[i]
            
            mem[i] = cost[i] + min(dp(i-1), dp(i-2))
            return mem[i]

        n = len(cost)
        return min(dp(n-1), dp(n-2))