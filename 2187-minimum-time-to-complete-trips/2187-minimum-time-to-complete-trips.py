class Solution:
    def check(self,mid,arr):
        total_sum = 0
        for num in arr:
            total_sum += (mid // num)
        return total_sum
        
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        low = min(time)
        high = totalTrips * low
        
        ans = 0
        while low <= high:
            mid = (low + high)//2
            
            if self.check(mid,time) >= totalTrips:
                ans = mid
                high = mid -1
            else:
                low  = mid + 1
                     
        return ans