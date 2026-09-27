
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * n
        if obstacleGrid[-1][-1]: # Check if destination is an obstacle
            return 0
        dp[-1] = 1

        for r in range(m - 1, -1, -1):
            # Right border case
            if obstacleGrid[r][-1]:
                dp[-1] = 0
                
            path_exists = bool(dp[-1])  # Short-circuit optimization
            for c in range(n - 2, -1, -1):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                    continue
                path_exists = True
                dp[c] += dp[c + 1]

            if not path_exists:
                break

        return dp[0]
