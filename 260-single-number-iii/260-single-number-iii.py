class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = 0
        for i in nums:
            ans ^= i

        diff = 0
        for diff in range(32):
            if (1 << diff ) & ans:
                break

        xor = 0
        for i in nums:
            if (1 << diff) & i:
                xor ^= i
                
        return [xor,xor^ans]
                
                
        
        