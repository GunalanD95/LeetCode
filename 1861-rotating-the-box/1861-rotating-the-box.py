class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])
        
        # for each stone move right in its row (before obs,stone)
        for row in range(rows):
            for col in range(cols-1,-1,-1):
                if box[row][col] != '#':
                    continue
                    
                sc = col+1

                found = False
                while sc < cols and box[row][sc] == '.':
                    found = True
                    sc += 1
                    
                if found:
                    box[row][col] = '.'
                    box[row][sc-1]   = '#'
                    

        # Create a new matrix with transposed dimensions
        arr = [[0] * rows for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                arr[col][row] = box[row][col]
                
        rotated = [row[::-1] for row in arr]
        print("rotated",rotated)
        
        return rotated
        
        