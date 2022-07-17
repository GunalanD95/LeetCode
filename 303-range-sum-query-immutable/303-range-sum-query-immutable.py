class NumArray:

    def __init__(self, nums: List[int]):
        N = len(nums)
        self.PF = [0] * N
        self.PF[0] =  nums[0]

        prev = nums[0]
        for i in range(1,N):
            self.PF[i] = nums[i] + prev
            prev =  self.PF[i]
        
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.PF[right]
        else:
            return self.PF[right] - self.PF[left-1]
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)