class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower,upper]]
        if lower == upper:
            return []
        
        
        N = len(nums)
        
        if N == 1:
            if lower <= nums[0] <= upper:
                if nums[0] == lower:
                    return [[nums[0] + 1, upper]]
                elif nums[0] == upper:
                    return [[lower, nums[0] - 1]]
                else:
                    return [[lower, nums[0] - 1], [nums[0] + 1, upper]]
        
        res = []
        if nums[0] > lower:
            res.append([lower, nums[0] - 1])        
        for i in range(1,N):
            if abs(nums[i-1] - nums[i]) <= 1:
                continue
            cur = [nums[i-1]+1,nums[i]-1]
            res.append(cur)
        
        if nums[-1] < upper:
            cur = [nums[N-1]+1,upper]
            res.append(cur)
        return res