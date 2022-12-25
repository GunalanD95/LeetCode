class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        ans = []
        for i in queries:
            val = i
            cur_sum = 0
            c = 0
            nums.sort()
            for j in range(len(nums)):
                if cur_sum + nums[j] <= val:
                    c +=1
                cur_sum += nums[j] 

            ans.append(c)
            
        return ans 