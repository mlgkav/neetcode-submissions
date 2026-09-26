class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        # (room available time, room number)
        rooms_heap = [(0, i) for i in range(n)] 
        meeting_count = [0] * n
        heapq.heapify(rooms_heap)

        for start, end in meetings:
            while rooms_heap and rooms_heap[0][0] < start:
                room_free, room = heapq.heappop(rooms_heap)
                heapq.heappush(rooms_heap, (start, room))

            room_free, room = heapq.heappop(rooms_heap)
            if room_free > start:
                end += room_free - start
            heapq.heappush(rooms_heap, (end, room))
            meeting_count[room] += 1
        return max(enumerate(meeting_count), key=lambda x: x[1])[0]


