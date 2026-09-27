class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    continue

                down = grid[r + 1][c] if r + 1 < m else float("inf")
                right = grid[r][c + 1] if c + 1 < n else float("inf")
                grid[r][c] += min(down, right)

        return grid[0][0]