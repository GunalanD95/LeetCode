class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_sum = sum(rolls)
        total_n   = len(rolls) + n
        
        # total_sum + missing_sum / total_n = mean
        
        missing_sum = (mean * total_n) - total_sum
        
        # Check if the missing sum can be distributed among n rolls
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        # Create the result array with all 1s
        res = [1] * n
        missing_sum -= n  # Subtract the 1s we already added to each roll     
        
        for idx,val in enumerate(res):
            if missing_sum == 0:
                break
            to_add = min(5,missing_sum)
            res[idx] +=to_add
            missing_sum -= to_add
            
        
        return res
        