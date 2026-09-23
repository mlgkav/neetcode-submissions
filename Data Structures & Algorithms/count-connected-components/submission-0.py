class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y: # x and y already within the same connected component (cycle)
                return False

            if rank[x] > rank[y]:
                parent[y] = x
            elif rank[y] > rank[x]:
                parent[x] = y
            else:
                parent[y] = x
                rank[x] += 1

            return True

        count = n
        for a, b in edges:
            if union(a, b):
                count -= 1

        return count
