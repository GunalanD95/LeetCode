class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        

        # binary search 
        A = matrix
        
        rows = len(A)
        cols = len(A[0])
        
        
        low = 0
        high = (rows * cols) - 1
        
        while low <= high:
            
            mid = (low + high) // 2
            
            rowidx = mid // cols
            colidx = mid % cols 
            
            if A[rowidx][colidx] == target:
                return True
            
            if A[rowidx][colidx] > target:
                high = mid - 1
                
            else:
                low = mid + 1
                
                
                
        return False 
    
        '''
        check striver video

        '''
        