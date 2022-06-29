class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] ==  target:
        #             return [i,j]       
        A , B = nums , target      
        hashmap = {}

        for i in range(len(A)):
            a = A[i]
            b = B - a
            
            if b in hashmap:
                return(hashmap.get(b),i)
            
            if A[i] not in hashmap:
                hashmap[A[i]] = i
        return []

            
            
        