class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
            

    def add(self, val: int) -> int:
        if len(self.min_heap) == self.k:
            if val > self.min_heap[0]:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, val)
        else:
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0]