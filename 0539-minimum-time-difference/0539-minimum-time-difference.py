from datetime import timedelta
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Sort the time points
        timePoints.sort()
        min_diff = float('inf')
        
        # Convert the first time point to timedelta
        h1, m1 = map(int, timePoints[0].split(":"))
        t1 = timedelta(hours=h1, minutes=m1)
        
        # Store the first time for circular comparison later
        first_time = t1

        for i in range(1, len(timePoints)):
            h2, m2 = map(int, timePoints[i].split(":"))
            t2 = timedelta(hours=h2, minutes=m2)
            
            # Calculate difference between adjacent time points
            result = t2 - t1
            total_minutes = int(result.total_seconds() // 60)
            min_diff = min(min_diff, total_minutes)
            
            t1 = t2
        
        # Compare the last time with the first to account for the circular nature of time
        last_time = t1
        circular_diff = (first_time + timedelta(days=1)) - last_time
        circular_minutes = int(circular_diff.total_seconds() // 60)
        min_diff = min(min_diff, circular_minutes)
        
        return min_diff
