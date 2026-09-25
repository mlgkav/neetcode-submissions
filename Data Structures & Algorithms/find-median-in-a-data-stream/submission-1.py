class MedianFinder:

    def __init__(self):
        self.top_heap = []
        self.bottom_heap = []
        

    def addNum(self, num: int) -> None:
        if len(self.top_heap) < len(self.bottom_heap):
            to_push = heapq.heappushpop(self.bottom_heap, -num)
            heapq.heappush(self.top_heap, -to_push)
        else:
            to_push = heapq.heappushpop(self.top_heap, num)
            heapq.heappush(self.bottom_heap, -to_push)

    def findMedian(self) -> float:
        if len(self.top_heap) < len(self.bottom_heap):
            return -self.bottom_heap[0]
        return (-self.bottom_heap[0] + self.top_heap[0]) / 2.0