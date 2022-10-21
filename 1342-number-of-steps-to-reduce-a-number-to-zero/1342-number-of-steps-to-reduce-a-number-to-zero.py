class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        def countsteps(num,count):
            if num == 0:
                return count
            
            if num & 1:
                num = num - 1
            else:
                num = num // 2
                
                
            return countsteps(num,count+1)
        
        
        
        count = countsteps(num,0)
        
        return count 
                
                
            
            
        