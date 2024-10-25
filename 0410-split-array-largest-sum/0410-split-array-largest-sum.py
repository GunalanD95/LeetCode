from collections import deque

class Solution:
    def check_possible(self,arr,sub_sum):
        cur_sum = 0
        total   = 1
        
        for num in arr:
            if sub_sum == 15:
                print(cur_sum,total,num)
            if cur_sum + num <= sub_sum:
                cur_sum += num
            else:
                total += 1
                if total > self.k:
                    return total
                cur_sum = num
        return total 
        
    def splitArray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        low  = max(nums)
        high = sum(nums)
        
        self.k = k
        
        min_sum = float('inf')
        while low < high:    
            mid = ( low + high)//2
            
            total_subs = self.check_possible(nums,mid)
            
            print("total_subs->",total_subs,"mid->",mid)
            
            if total_subs > k:
                low  = mid + 1
            else:
                if total_subs == k:
                    min_sum = mid
                high = mid 
            
        
        return low
        