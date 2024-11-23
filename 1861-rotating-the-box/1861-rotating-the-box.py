class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])
        
        # Simulate gravity for each row
        for row in range(rows):
            empty_pos = cols - 1  # Start at the rightmost position
            for col in range(cols - 1, -1, -1):
                if box[row][col] == '#':  # Stone
                    box[row][col] = '.'  # Remove stone from current position
                    box[row][empty_pos] = '#'  # Move stone to the farthest right position
                    empty_pos -= 1  # Update empty position
                elif box[row][col] == '*':  # Obstacle
                    empty_pos = col - 1  # Reset empty position to left of obstacle
                    

        # Create a new matrix with transposed dimensions
        arr = [[0] * rows for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                arr[col][row] = box[row][col]
                
        rotated = [row[::-1] for row in arr]
        print("rotated",rotated)
        
        return rotated
        
        