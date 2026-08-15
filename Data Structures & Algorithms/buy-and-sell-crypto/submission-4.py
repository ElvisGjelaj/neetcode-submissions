class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestbuy = 0
        bestprofit = prices[0]
        for price in prices:
            if price < bestbuy:
                bestbuy = price
            currprofit = price - bestbuy
            if currprofit > bestprofit: 
                bestprofit = currprofit

        if bestprofit < 0: 
            return 0
        else: 
            return bestprofit 