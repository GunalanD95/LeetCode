class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set(nums)
        
        N    = len(nums)
        
        ans  = ''            
        for binary_string in nums:
            cur_string = [char for char in binary_string]

            for idx,bit in enumerate(binary_string):
                if bit == '1':
                    cur_string[idx] = '0'
                else:
                    cur_string[idx] ='1'

                if "".join(cur_string) not in seen:
                    return "".join(cur_string)
                
        return ans
                    
           
                    