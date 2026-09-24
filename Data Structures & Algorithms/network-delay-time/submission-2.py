class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for source, target, travel_time in times:
            adj_list[source].append((target, travel_time))

        min_heap = [(0, k)]
        visited = set()
        max_time = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)

            # Skip if already visited
            if node in visited:
                continue

            # Process newly visited node
            visited.add(node)
            max_time = time

            # Early exit optimization: stop if all nodes are reached
            if len(visited) == n:
                return max_time

            # Push neighbors
            for neighbor, travel_time in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + travel_time, neighbor))

        return max_time if len(visited) == n else -1