class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        i = int(ord(coordinates[0]) - ord('a')) + 1
        j = int(coordinates[1])
        
        # white
        if i % 2 == 0 and j % 2 == 0:
            return False
        elif i % 2 != 0 and j % 2 != 0:
            return False
        elif i % 2 == 0 and j % 2 != 0:
            return True
        else:
            return True