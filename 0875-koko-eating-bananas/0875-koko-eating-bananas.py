class Solution:
    def check(self,mid,piles,h):
        total_count = 0
        for num in piles:
            value = math.ceil(num/mid)              
            total_count += value
        return True if total_count <= h else False
                
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low   = 1
        high  = max(piles)
        ans   = high
        while low <= high:
            mid = (low + high)//2
            print("mid",mid)
            if self.check(mid,piles,h):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
                
        return ans
            
        