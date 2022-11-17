class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        N   = len(candidates)
        candidates.sort()
        def subbsetSum(indx,arr,curSum):
            if indx == N:
                if curSum == target:
                    temp = arr.copy()
                    res.append(temp)
                return
            
            if curSum > target:
                return
            
            # take it 
            arr.append(candidates[indx])
            curSum += candidates[indx]
            
            subbsetSum(indx+1,arr,curSum)
            
            # skipping duplicates for right side call 
            while indx < N-1 and candidates[indx] == candidates[indx+1]:
                indx += 1
            
            # dont take it and backtrack 
            curSum -= candidates[indx]
            arr.pop()
            subbsetSum(indx+1,arr,curSum)
            
        
        subbsetSum(0,[],0)
        return res
        