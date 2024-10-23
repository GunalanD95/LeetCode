from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        memo = [[-1] * cols for _ in range(rows)]
        
        def dfs(row: int, col: int) -> int:
            if memo[row][col] != -1:
                return memo[row][col]
            
            max_length = 1
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    max_length = max(max_length, 1 + dfs(new_row, new_col))
            
            memo[row][col] = max_length
            return max_length
        
        longest_path = 0
        for i in range(rows):
            for j in range(cols):
                longest_path = max(longest_path, dfs(i, j))
        
        return longest_path