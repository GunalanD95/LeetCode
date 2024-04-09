class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]  # Count of students preferring each type of sandwich
        
        for student in students:
            count[student] += 1
        
        for sandwich in sandwiches:
            if count[sandwich] == 0:
                break  # No more students prefer this type of sandwich
            count[sandwich] -= 1
        
        return sum(count)