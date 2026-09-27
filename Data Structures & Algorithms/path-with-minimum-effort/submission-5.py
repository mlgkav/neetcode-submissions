class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Kruskall's + DSU solution
        m, n = len(heights), len(heights[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        min_heap = []
        for r in range(m):
            for c in range(n):
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    effort = abs(heights[r][c] - heights[nr][nc])
                    # c
                    min_heap.append((effort, r*n + c, nr*n + nc)) 
        heapq.heapify(min_heap)

        parent = [r*n + c for r in range(m) for c in range(n)]
        size = [1] * m*n

        def find(node):
            while parent[node] != node:
                parent[node] = node = parent[parent[node]]
            return node

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False

            if size[pu] < size[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            size[pu] += size[pv]
            return True

        while min_heap:
            effort, u, v = heapq.heappop(min_heap)
            if union(u, v) and find(0) == find(m*n - 1):
                return effort
        return 0