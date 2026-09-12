class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        fresh_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        t = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc
                    if (0 <= new_r < m and 0 <= new_c < n
                        and grid[new_r][new_c] == 1):
                        print(new_r, new_c)
                        grid[new_r][new_c] = 2
                        fresh_count -= 1
                        q.append((new_r, new_c))
            if q:
                t += 1
                


        return t if fresh_count == 0 else -1
