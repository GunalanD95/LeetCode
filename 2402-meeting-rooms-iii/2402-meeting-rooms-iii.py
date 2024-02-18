class Solution:
    def mostBooked(self, num_rooms, meetings):
        available_rooms = [room for room in range(num_rooms)]
        occupied_rooms = []
        heapify(available_rooms)
        booking_counts = [0] * num_rooms

        sorted_meetings = sorted(meetings, key=lambda x: x[0])
        for start_time, end_time in sorted_meetings:
            while occupied_rooms and occupied_rooms[0][0] <= start_time:
                end, room = heappop(occupied_rooms)
                heappush(available_rooms, room)

            if available_rooms:
                room = heappop(available_rooms)
                heappush(occupied_rooms, [end_time, room])
            else:
                current_end, room = heappop(occupied_rooms)
                new_end = current_end + end_time - start_time
                heappush(occupied_rooms, [new_end, room])
            booking_counts[room] += 1
        max_booking_count = max(booking_counts)
        most_booked_room = booking_counts.index(max_booking_count)
        return most_booked_room