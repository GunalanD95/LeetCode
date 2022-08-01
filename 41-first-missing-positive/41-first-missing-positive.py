class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        # BruteForce - Linear Search - O(n)2
        N = len(nums)
        i = 0

        while i < N:
            if nums[i] > 0 and nums[i] < N +1:
                correctindx = nums[i] - 1
                if nums[correctindx] != nums[i]:
                    temp = nums[i]
                    nums[i] = nums[correctindx]
                    nums[correctindx] = temp
                else:
                    i+= 1

            else:
                i +=1
                
        for i in range(N):
            if nums[i]-1 != i:
                return(i+1)
            
            
        return N+1

                
                
        