class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        pre = [1] * N
        
        for idx in range(1,N):
            pre[idx] = pre[idx-1] * nums[idx-1]
            
        print("pre",pre)
        
        suf = [1] * N
        for idx in range(N-2,-1,-1):
            suf[idx] =  suf[idx+1] * nums[idx+1]
        
        print("suf-2",suf)
        
        ans = []
        
        for v1,v2 in zip(pre,suf):
            ans.append(v1*v2)
        
        return ans
        