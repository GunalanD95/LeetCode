class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        total_diff = 0
        for val1,val2 in zip(seats,students):
            total_diff += abs(val1 - val2)
        return total_diff