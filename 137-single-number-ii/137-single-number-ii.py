class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0
        N = len(nums)
        
        for i in range(32):
            mask = 1 << i    
            count = 0
            for j in range(N):
                if mask & nums[j]:
                    count += 1
                    
            val = count % 3
            
            ans |= (val<<i)
            
            
        return self.convert(ans)
    
    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x