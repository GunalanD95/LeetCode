class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        L  , R =  0, 0
        for num in nums:
            if num ==  0:
                continue 
            if num < 0:
                L += 1
            else:
                R += 1
        return max(L,R)