class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right = prices[0], 0
        maxProfit = 0
        profit = 0

        for i in range(len(prices) - 1):
            right = prices[i + 1]

            if left > right:
                left = right
            
            profit = right - left
            if profit > maxProfit:
                maxProfit = profit
        
        return maxProfit



        