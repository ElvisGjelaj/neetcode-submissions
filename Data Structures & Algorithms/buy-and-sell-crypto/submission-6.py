class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestbuy = prices[0]
        bestprofit = 0
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