class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_price = float("inf")
        res = 0
        for p in prices:
            res = max(res, p - min_buy_price)
            min_buy_price = min(min_buy_price, p)
        return res