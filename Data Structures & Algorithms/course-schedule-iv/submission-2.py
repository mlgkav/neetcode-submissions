class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = []
        adj = [[False] * numCourses for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adj[pre][crs] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    adj[i][j] = adj[i][j] or (adj[i][k] and adj[k][j])

        for u, v in queries:
            res.append(adj[u][v])

        return res