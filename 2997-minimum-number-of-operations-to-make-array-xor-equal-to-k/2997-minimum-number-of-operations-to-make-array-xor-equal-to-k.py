class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        N   = len(nums)
        xor = 0
        for num in nums:
            xor ^= num
            
        result = xor ^ k
        
        print(result , xor ,k)
        
        diffbits = 0
        while result:
            diffbits += result & 1
            result >>= 1

        return diffbits