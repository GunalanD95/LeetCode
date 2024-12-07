class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def check(penalty):
            operations = 0
            for num in nums:
                operations += (num - 1) // penalty
                if operations > maxOperations:
                    return False
            return True            
            
            return True
        
        
        
        left , right = 1 , max(nums)
        ans = right
        
        
        while left <= right:
            mid = (left + right)//2
            
            if check(mid):
                ans = mid
                right = mid -1
            else:
                left   = mid +1

        return ans
        