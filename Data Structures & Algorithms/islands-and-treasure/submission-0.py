class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m, n = len(grid), len(grid[0])

        # Add all the treasure tests to the queue
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # Perform a BFS from each of the treasure chests, where closest distance = level
        level = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            level += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                
                # Check the adjacent cells
                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc


                    if (0 <= new_r < m and 0 <= new_c < n
                        and grid[new_r][new_c] == 2147483647):
                        grid[new_r][new_c] = level
                        q.append((new_r, new_c))
