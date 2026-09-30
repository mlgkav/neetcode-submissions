class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # path with min elevation
        m, n = len(grid), len(grid[0])

        visited = set((0, 0))
        min_heap = [(grid[0][0], 0, 0)]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while True:
            max_path_elevation, r, c = heapq.heappop(min_heap)

            # Check if bottom right cell reached
            if r == m - 1 and c == n - 1:
                return max_path_elevation

            # Iterate through adjacent cells
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr >= m or nc < 0 or nc >= n
                    or (nr, nc) in visited
                ):
                    continue
                visited.add((nr, nc))
                heapq.heappush(min_heap, (max(max_path_elevation, grid[nr][nc]), nr, nc))


