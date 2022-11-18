class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        N   = len(candidates)
        
        def Combination(indx,arr,curSum):
            if curSum > target:
                return 
            
            if curSum == target:
                temp = arr.copy()
                res.append(temp)
                return
            
            for i in range(indx,N):
                curSum += candidates[i]
                arr.append(candidates[i])
                Combination(i,arr,curSum)
                
                curSum -= candidates[i]
                arr.pop()
            
        
        Combination(0,[],0)
        
        return res
        