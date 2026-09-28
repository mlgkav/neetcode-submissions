class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0

        visited = [False] * n
        distance = [float("inf")] * n
        node = 0
        result = 0

        for _ in range(n - 1):
            visited[node] = True
            next_node = -1

            for neighbor in range(n):
                if visited[neighbor]:
                    continue

                cost = (abs(points[node][0] - points[neighbor][0])
                        + abs(points[node][1] - points[neighbor][1]))
                distance[neighbor] = min(distance[neighbor], cost)

                if next_node == -1 or distance[neighbor] < distance[next_node]:
                    next_node = neighbor

            result += distance[next_node]
            node = next_node

        return result