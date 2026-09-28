from functools import cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(l, r):
            if l > r:
                return 0
            left, right = piles[l], piles[r]
            if r - l % 2 == 0:
                left *= -1
                right *= -1
            return max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)

        return dfs(0, len(piles) - 1) > 0