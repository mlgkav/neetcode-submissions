class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1 ,-1):
                dp[c] += dp[c + 1]

        return dp[0]