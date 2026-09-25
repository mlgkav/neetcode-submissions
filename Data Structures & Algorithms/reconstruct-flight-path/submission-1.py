class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_heap = defaultdict(list)
        for src, dest in tickets:
            heapq.heappush(adj_heap[src], dest)

        res = []
        def dfs(node):
            while adj_heap[node]:
                dfs(heapq.heappop(adj_heap[node]))
            res.append(node)

        dfs("JFK")
        res.reverse()
        return res