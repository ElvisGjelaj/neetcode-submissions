class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            dp[i] = min((dp[i - c] + 1 for c in coins if i - c >= 0), default=float("inf"))
        print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1