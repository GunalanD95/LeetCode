class Solution:
    
    def mycmp(self, a, b): 
        str_a = str(a)
        str_b = str(b)
        
        l1,l2 = 0 , 0
        while l1 < len(str_a) and l2 < len(str_b):
            if str_a[l1] > str_b[l2] :
                return 1
            elif str_a[l1]  < str_b[l2] :
                return -1
            l1 +=1
            l2 +=1
            
        if len(str_a) > len(str_b):
            return 1
        elif len(str_a) < len(str_b):
            return -1
            
        return 0
        
    
    def lexicalOrder(self, n: int) -> List[int]:
        
        nums = [i for  i in range(1,n+1)]
        ans  = sorted(nums, key=functools.cmp_to_key(self.mycmp))
        return ans
        
        