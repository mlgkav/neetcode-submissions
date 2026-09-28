class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [0] * n

        for l in reversed(range(n)):
            for r in range(l, n):
                even = ((r - l) % 2 == 0)
                left = piles[l] if even else 0
                right = piles[r] if even else 0

                if l == r:
                    dp[r] = left
                else:
                    dp[r] = max(dp[r] + left, dp[r - 1] + right)

        total = sum(piles)
        alice_score = dp[n - 1]
        return alice_score > (total - alice_score)