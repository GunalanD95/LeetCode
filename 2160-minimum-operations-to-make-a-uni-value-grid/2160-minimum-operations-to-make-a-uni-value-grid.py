class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = []
        remainder = grid[0][0] % x  # Store the remainder of the first element

        for row in grid:
            for num in row:
                if num % x != remainder:  # Check feasibility across the entire grid
                    return -1
                values.append(num // x)  # Convert numbers into "step form"

        values.sort()
        median = values[len(values) // 2]

        return sum(abs(num - median) for num in values)