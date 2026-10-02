import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted([(query, j) for j, query in enumerate(queries)])
        min_lengths = [] # (interval_length, interval_end)

        i = 0
        res = [-1] * len(queries)
        for query, j in sorted_queries:
            # Add intervals that are alive at query
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(min_lengths, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            # Ensure that the shortest interval is currently alive
            while min_lengths and min_lengths[0][1] < query:
                heapq.heappop(min_lengths)
            
            if min_lengths:
                res[j] = min_lengths[0][0]

        return res