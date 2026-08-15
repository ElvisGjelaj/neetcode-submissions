class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestbuy = 0
        bestprofit = 0
        for price in prices:
            if price < bestbuy:
                bestbuy = price
            else: 
                bestprofit = price - bestbuy 
        if bestprofit < 0: 
            return 0
        else: 
            return bestprofit 