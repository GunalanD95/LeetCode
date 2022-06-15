class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        A = nums
        for i in range(len(A)):
            if A[i] not in dic:
                dic[A[i]] = 1
            else:
                dic[A[i]] = 2

        res = []
        for j in dic:
            if dic[j] == 1:
                res.append(j)


        return(res)
                
                
        
        