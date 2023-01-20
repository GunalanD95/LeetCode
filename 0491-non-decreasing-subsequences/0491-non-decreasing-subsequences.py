class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        arr = []
        
        
        def recorBro(indx,prev):
            if indx >= len(nums):
                if len(arr) >= 2:
                    res.add(tuple(arr))
                    
                return
            
            # dont_take
            recorBro(indx+1,prev)
            
            # take_it
            if nums[indx] >= prev:
                arr.append(nums[indx])
                recorBro(indx+1,nums[indx])
                arr.pop()
                
        
        recorBro(0,-inf)
        return list(res)
            
            
            
        