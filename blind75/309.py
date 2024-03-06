class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def profit(i, can_buy):
            if i >= len(prices):
                return 0
            
            if (i, can_buy) in memo: return memo[(i, can_buy)]
            
            if can_buy:
                buy_profit = profit(i + 1, not can_buy) - prices[i]
                cool_profit = profit(i + 1, can_buy)
                memo[(i, can_buy)] = max(buy_profit, cool_profit)
            else:
                sell_profit = profit(i + 2, not can_buy) + prices[i]
                cool_profit = profit(i + 1, can_buy)
                memo[(i, can_buy)] = max(sell_profit, cool_profit)
            
            return memo[(i, can_buy)]

        return profit(0, True)