class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        return len(set((y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf') for ((x1, y1), (x2, y2)) in zip(coordinates, coordinates[1:]))) == 1