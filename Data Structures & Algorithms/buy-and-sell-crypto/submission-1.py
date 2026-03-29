class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        for cur_price in prices:
            max_profit = max(max_profit, cur_price - min_buy)
            min_buy = min(min_buy, cur_price)
        return max_profit
