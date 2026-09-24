class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((v, t))

        min_heap = [(0, k)]
        visited = set()
        while len(visited) != n and min_heap:
            # Find next univisted node
            while min_heap: 
                time, u = heapq.heappop(min_heap)
                if u not in visited:
                    break

            # Process its unvisited neighbors
            visited.add(u)
            for v, t in adj_list[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (time + t, v))

        return time if len(visited) == n else -1