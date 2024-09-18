from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        nums = self.timestamps[key]
        if len(nums) == 0 or nums[0][0] > timestamp:
            return ''
        
        low , high  = 0 , len(nums) - 1
        
        ans = -1
        
        while low <= high:
            mid = (low + high)//2
            
            time , value = nums[mid]
            if time <= timestamp:
                ans = value
                # look for smaller index on the left
                low = mid + 1
            else:
                high = mid - 1  # look on the right

        return ans

            
