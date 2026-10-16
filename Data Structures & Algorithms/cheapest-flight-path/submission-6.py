class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k + 1):
            temp_prices = prices[:]
            for start, end, price in flights:
                temp_prices[end] = min(temp_prices[end], prices[start] + price)
            prices = temp_prices

        return -1 if prices[dst] == float("inf") else prices[dst]
