class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        N = len(nums)
        ans = 0
        c = 0
        indx = []
        jndx = []
        for i in range(N):
            for j in range(i+1,N):
                if nums[i] + diff == nums[j]:
                    indx.append(i)
                    jndx.append(j)



        val = list(set(indx) & set(jndx))
        
        return len(val)