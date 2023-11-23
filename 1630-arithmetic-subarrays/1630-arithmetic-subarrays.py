class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
                
        res = []
        
        for i,j in zip(l,r):
            val = nums[i:j+1]
            val.sort()
            
            if len(val) == 2:
                res.append(True)
            else:
                diff = val[1] - val[0]
                is_good = True
                for i in range(2,len(val)):
                    cur_diff = val[i] - val[i-1]
                    
                    if cur_diff != diff:
                        is_good = False
                        break
                        
                if is_good:
                    res.append(True)
                else:
                    res.append(False)
            
        return res  
        