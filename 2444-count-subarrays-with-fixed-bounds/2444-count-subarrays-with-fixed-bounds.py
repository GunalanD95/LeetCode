class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        firstMax = None
        firstMin = None
        firstBad = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                firstBad = i
            if nums[i] == minK:
                firstMin = i
            if nums[i] == maxK:
                firstMax = i
            if firstMin != None and firstMax != None:
                lastStart = min(firstMin, firstMax)
                if firstBad < lastStart:
                    count += lastStart - firstBad
        return count