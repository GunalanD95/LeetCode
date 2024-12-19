class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = float('-inf')
        max_chunks = 0
        
        for idx,num in enumerate(arr):
            max_so_far = max(max_so_far,num)    
            if max_so_far == idx:
                max_chunks += 1
        return max_chunks
        