class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        N = len(nums)
        
        def backtrack(arr,nums,indx):
            # base condition
            if indx == N:
                temp_arr = arr.copy()
                res.append(temp_arr)
                return
            
            # take the cur indx
            print(arr,indx)
            arr.append(nums[indx])
            backtrack(arr,nums,indx+1)
            
            
            # ignore duplicates 
            while  indx < N-1 and nums[indx] == nums[indx+1]:
                indx += 1
            
            # dont take -> backtrack
            arr.pop()
            backtrack(arr,nums,indx+1)
        temp = []
        backtrack(temp,nums,0)
        
        res.sort()
        
        return res
        