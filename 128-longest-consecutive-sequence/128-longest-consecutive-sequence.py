class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)

        ans = 0
        for i in hset:
            x = i 
            prev_elem = x - 1
            
            if prev_elem not in hset:
                count = 0
                while x in hset:
                    x = x + 1
                    count += 1
                ans = max(ans,count) 


        return ans        