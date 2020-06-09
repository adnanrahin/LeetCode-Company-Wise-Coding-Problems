class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        buy_ = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy_:
                buy_ = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - buy_)
        return max_profit
