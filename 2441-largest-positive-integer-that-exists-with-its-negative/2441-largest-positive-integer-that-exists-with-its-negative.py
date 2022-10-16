class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        nums  = set(nums)
        
        hashmap = defaultdict(int)
        
        for i in nums:
            val = abs(i)
            hashmap[val] += 1
            
        ans = float('-inf')
        for j in hashmap:
            if hashmap[j] == 2:
                ans = max(j,ans)
                
        if ans == float('-inf'):        
            return -1 
        
        return ans
            
            
        
        