from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(day, coin_owned):
            if day >= len(prices):
                return 0

            cooldown = 2 if coin_owned else 1
            profit = prices[day] if coin_owned else -prices[day]
            return max(profit + dfs(day + cooldown, not coin_owned), dfs(day + 1, coin_owned))

        return dfs(0, False)