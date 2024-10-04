class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        
        rng = 1 << N
        
        def checkbit(n,j):
            if (1 << j) & n:
                return True
            return False
        
        res = []
        for i in range(rng):
            cur = []
            for j in range(N):
                if checkbit(i,j):
                    cur.append(nums[j])
            res.append(cur)
        return res
        
        
        