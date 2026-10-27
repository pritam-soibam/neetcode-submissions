class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # [10,1,5,6,7,1]
        buy = prices[0]
        for sell in prices[1:]:
            profit = max(profit, sell - buy)
            buy = min(sell, buy)

        return profit
