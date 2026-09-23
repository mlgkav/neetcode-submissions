class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_map = defaultdict(list)
        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)
        
        visited = set()
        def dfs(n, par):
            if n in visited:
                return False

            visited.add(n)
            for nei in adj_map[n]:
                if nei != par and not dfs(nei, n):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n