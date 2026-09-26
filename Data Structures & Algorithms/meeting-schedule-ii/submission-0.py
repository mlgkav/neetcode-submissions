"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: (i.start, i.end))

        res = 0
        min_heap = []
        for interval in intervals:
            while min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
            res = max(res, len(min_heap))

        return res
        
