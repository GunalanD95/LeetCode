class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        ans = [0] * N
        
        pos =  0
        neg =  1
        for i in nums:
            if i > 0:
                ans[pos] = i
                pos += 2
                
            else:
                ans[neg] = i
                neg += 2
                
        return ans 
        
        '''
        - bruteforce : *using two negative and postive arrays we are just segrigating them and then adding them to our ans array *
          tc : o(N)
          
          
          
        - optimized :
        
            we can find pos of postive and negative using variables :
            pos += 2
            neg += 2 , when we find pos or neg 

        '''
        
        
