from collections import *
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = deque()
        q.append((0,0))
        
        n = len(nums)
        
        
        res = []
        
        while q:
            row , col = q.popleft()
            
            res.append(nums[row][col])
            
            if col == 0 and row + 1 < n:
                q.append((row+1,col))
        
            if col + 1 < len(nums[row]):
                q.append((row,col+1))
            
        return res