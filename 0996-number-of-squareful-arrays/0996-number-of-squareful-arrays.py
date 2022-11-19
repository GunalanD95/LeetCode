from collections import Counter
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        CountMap = Counter(nums)  #  using count map to avoid duplicates
        N = len(nums)
        self.count = 0
        def isPerfectSquare(num):
            return pow(int(sqrt(num)), 2) == num

        
        def _dfs(indx,arr):
            # base cases 
            
            # i-check last two added numbers sum are perfect square
            if len(arr) > 1:
                if not isPerfectSquare(arr[-1] + arr[-2]):
                    return
                
            # ii-we reached end so c++
            if indx == N:
                self.count += 1            
                return
                
            for i in CountMap:
                if CountMap[i] > 0:
                    # take duplicates
                    arr.append(i)
                    CountMap[i] -= 1
                    
                    _dfs(indx+1,arr)
                
                    # undo it and dont take duplicates
                    CountMap[i] += 1
                    arr.pop()

        _dfs(0,[])
        return self.count