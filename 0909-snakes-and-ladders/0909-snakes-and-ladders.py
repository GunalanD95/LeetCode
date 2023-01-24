from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        
        def helper(square):
            square = square - 1
            
            r = square // n
            c = square % n
            
            if r &1 :
                c = n - 1 - c
            return [r,c]
            
        
        q = deque()
        q.append([1,0])
        hashset = set()
        
        while q:
            cur_node , distance = q.popleft()
            
            if cur_node == (n*n):
                return distance
            
            
            for i in range(1,7):
                nextSqr = cur_node + i
                r , c   = helper(nextSqr)
                
                if board[r][c] != -1:
                    nextSqr = board[r][c]
                    
                if nextSqr == n*n:
                    return distance + 1
                
                if nextSqr not in hashset:
                    hashset.add(nextSqr)
                    q.append([nextSqr,distance+1])

        return -1
                
        