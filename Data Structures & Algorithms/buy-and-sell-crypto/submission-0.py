class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        sell = 0
        for i in range(1, len(prices)):
            sell = max(sell, prices[i] - lowest)
            lowest = min(lowest, prices[i])
        return sell
            


        