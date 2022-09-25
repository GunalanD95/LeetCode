class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        prefix = [0] * n 
        suffix = [0] * n

        prev1 = nums[0]
        count1 = 0
        for i in range(n):
            prefix[i] = count1
            
            if i != 0 and prev1 >= nums[i]:
                count1 += 1
            else:
                count1 = 1

            prev1 = nums[i]
            

        prev2 = nums[-1]
        count2 = 0
        for j in range(n-1,-1,-1):
            suffix[j] = count2
            
            if j != n-1 and prev2 >= nums[j]:
                count2 += 1
            else:
                count2 = 1

            prev2 = nums[j]
            


        ans = []

        for i in range(len(nums)):
            if suffix[i] >= k and prefix[i] >= k:
                ans.append(i)

        return ans         