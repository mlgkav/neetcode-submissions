class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        size = [1] * (len(edges) + 1)

        def find(node):
            # Path compression by half
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(a, b):
            root_a, root_b = find(a), find(b)

            if root_a == root_b:
                return False

            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
        
