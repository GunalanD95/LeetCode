class MyCalendarTwo:
    
    def __init__(self):
        self.bookings = []
        self.overlaps = []
    
    def book(self, start: int, end: int) -> bool:
        # Check if the new event would cause a triple booking by comparing with overlaps
        for overlap_start, overlap_end in self.overlaps:
            if start < overlap_end and end > overlap_start:  # If they overlap
                return False
        
        # If no triple booking, check for double booking and add to overlaps
        for booking_start, booking_end in self.bookings:
            if start < booking_end and end > booking_start:  # If they overlap
                # Add the overlap of this booking with the new event to the overlap list
                self.overlaps.append((max(start, booking_start), min(end, booking_end)))
        
        # Add the new event to bookings
        self.bookings.append((start, end))
        
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
