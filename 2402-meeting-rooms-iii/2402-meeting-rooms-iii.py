import heapq

class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # Sort meetings by start time
        meetings.sort()

        # Min-heap of available room numbers
        available = list(range(n))
        heapq.heapify(available)

        # Min-heap of busy rooms: (end_time, room_number)
        busy = []

        # Count of meetings per room
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free rooms that have finished by 'start'
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                # Assign immediately
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # Delay meeting
                finish_time, room = heapq.heappop(busy)
                heapq.heappush(busy, (finish_time + duration, room))

            count[room] += 1

        # Return room with max meetings (smallest index on tie)
        return count.index(max(count))
