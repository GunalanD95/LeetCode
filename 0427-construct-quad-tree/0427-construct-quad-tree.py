"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        if n == 0:
            return None
        
        def BuildTree(x1,y1,x2,y2):
            if x1 == x2 and y1 == y2:
                return Node(grid[x1][y1],True,None,None,None,None)
            
            mid_x = (x1 + x2)//2
            mid_y = (y1 + y2)//2
            
            topLeft = BuildTree(x1, y1, mid_x, mid_y)
            topRight = BuildTree(x1, mid_y + 1, mid_x, y2)
            bottomLeft = BuildTree(mid_x + 1, y1, x2, mid_y)
            bottomRight = BuildTree(mid_x + 1, mid_y + 1, x2, y2)
            
            # Check if all children are leaves with the same value
            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(None, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return BuildTree(0, 0, n - 1, n - 1)
            
            
        