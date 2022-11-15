class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N   = len(nums)
        
        
        def generatePermuation(arr,indx):
            # base case
            if indx == N:
                temp = arr.copy()
                res.append(temp)
                return
            
            for i in range(indx,N):
                # swap indx
                arr[i] , arr[indx] = arr[indx] , arr[i] 
                
                generatePermuation(arr,indx + 1)
                # swap em back to maintain for next call
                arr[i] , arr[indx] = arr[indx] , arr[i] 
            
        
        generatePermuation(nums,0)
        return res
        
        