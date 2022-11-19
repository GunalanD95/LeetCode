from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        CountMap = Counter(nums)
        result   = []
        N = len(nums)
        
        def _dfs(indx,arr):
            # base case
            if indx == N:
                result.append(arr.copy())
                return
                
            for i in CountMap:
                # take duplicates
                if CountMap[i] > 0:
                    arr.append(i)
                    CountMap[i] -= 1
            
                    _dfs(indx+1,arr)
                
                    # undo it 
                    CountMap[i] += 1
                    arr.pop()
            
            
            
            
            
        _dfs(0,[])
        return result
        