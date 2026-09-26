class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        unused_heap = [i for i in range(n)]
        heapq.heapify(unused_heap)
        in_use_heap = []
        room_to_meeting_count = [0] * n

        for start, end in meetings:
            while in_use_heap and in_use_heap[0][0] <= start:
                _, room = heapq.heappop(in_use_heap)
                heapq.heappush(unused_heap, room)

            if not unused_heap:
                prev_end, room = heapq.heappop(in_use_heap)
                end += prev_end - start
                heapq.heappush(unused_heap, room)

            room = heapq.heappop(unused_heap)
            room_to_meeting_count[room] += 1
            heapq.heappush(in_use_heap, (end, room))

        return max(enumerate(room_to_meeting_count), key=lambda x: x[1])[0]
        """
        47. 42
        [2, 2]
        """