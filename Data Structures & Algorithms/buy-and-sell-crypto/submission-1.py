class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far, profit = prices[0], 0

        for i in range(len(prices)):
            min_so_far = min(min_so_far, prices[i])
            profit = max(profit, prices[i]-min_so_far)
        return profit