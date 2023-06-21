class Solution:
    def calculateSum(self, nums, cost, target):
        res = 0
        for n, c in zip(nums, cost):
            res += abs(n - target) * c
        return res
    
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        s, e = min(nums), max(nums)
        
        while s < e:
            mid = (s + e) // 2
            leftSum, rightSum = self.calculateSum(nums, cost, mid), self.calculateSum(nums, cost, mid + 1)
            if leftSum < rightSum:
                e = mid
            else:
                s = mid + 1
        
        return self.calculateSum(nums, cost, s)