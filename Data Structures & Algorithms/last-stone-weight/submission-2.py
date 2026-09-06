from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapify(max_heap)

        while len(max_heap) > 1:
            x, y = heappop(max_heap), heappop(max_heap)
            if x == y:
                continue

            # x is always the larger stone
            heappush(max_heap, x - y)

        return -max_heap[0] if max_heap else 0