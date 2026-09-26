class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        min_heap = [(0, 0, 0)]  # (effort, r, c)
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == m - 1 and c == n - 1:
                return effort

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(min_heap, (new_effort, nr, nc))