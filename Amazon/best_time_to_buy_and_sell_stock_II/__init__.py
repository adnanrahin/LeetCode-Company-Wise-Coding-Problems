class Solution(object):
    def maxProfit(self, prices):
        total_profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                total_profit += prices[i + 1] - prices[i]

        return total_profit
