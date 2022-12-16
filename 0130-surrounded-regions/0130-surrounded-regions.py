from collections import deque , defaultdict

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N , M = len(board) , len(board[0])
        q = deque()
        visited  = [[False]* M for _ in range(N)]        
        hashmap = defaultdict(set) 
        for i in range(N):
            for j in range(M):
                if i == 0 or i == N-1 or j == 0 or j == M-1:
                    if board[i][j] == "O":
                        q.append((i,j))
                        visited[i][j]  = True
                        hashmap[(i,j)] = 1
                                  
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            row , col  = q.popleft()
            for i , j in directions:
                cr = row + i
                cc = col + j
                if cr < 0 or cr >= N or cc < 0 or cc >= M or visited[cr][cc] or board[cr][cc] == "X":
                    continue 
                visited[cr][cc]  = True
                hashmap[(cr,cc)] = 1
                q.append((cr,cc))

        for i in range(N):
            for j in range(M):
                if not visited[i][j]:
                    board[i][j] = "X"
                    
                
                    
                
                
        