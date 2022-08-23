class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        if N == 2:
            nums.sort(reverse=True)
            
        negati =[]
        posti =[]

        for i in range(len(nums)):
            if nums[i] < 0:
                negati.append(nums[i])
            else:
                posti.append(nums[i])


        ans = []
        while len(negati) > 0 and len(posti) > 0:
            ans.append(posti.pop(0))
            ans.append(negati.pop(0))
            
        return ans
        
        
        
