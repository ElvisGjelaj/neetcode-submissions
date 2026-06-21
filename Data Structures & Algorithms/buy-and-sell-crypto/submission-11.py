class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell =  0, 1
        maxProfit = 0

        while sell < len(prices):
            currProfit = prices[sell] - prices[buy]
            if prices[sell] > prices[buy]:
                maxProfit = max(currProfit, maxProfit)
            else:
                buy = sell
            sell += 1
        
        return maxProfit