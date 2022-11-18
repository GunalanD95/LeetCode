class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def combinations(indx,arr):
            if len(arr) == k:
                tempArr = arr.copy()
                ans.append(tempArr)
                return 
                
            else:    
                for i in range(indx,n+1):
                    arr.append(i)
                    combinations(i+1,arr)
                    arr.pop()
            
        combinations(1,[])    
        return ans
        