class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minprice = 999999
        maxprofit = 0
        for i in range(0,len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            
            currentprofit = prices[i] - minprice

            if currentprofit > maxprofit:
                maxprofit = currentprofit
            

        return maxprofit