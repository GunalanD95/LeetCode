class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        prev = None
        
        res = []
        
        cur = ''
        
        min_val , max_val = float('inf'), float('-inf')
        
        for num in nums:
            if prev == None:
                diff = 1
            else:
                diff = abs(num - prev)
            
            if diff == 1:
                pass
            else:
                if min_val != max_val:
                    cur = str(min_val) + '->' + str(max_val)
                else:
                    cur = str(min_val)
                res.append(cur)
                min_val , max_val = float('inf'), float('-inf')
            
            prev = num
            min_val = min(min_val,num)
            max_val = max(max_val,num)
       
        if min_val != max_val:
            cur = str(min_val) + '->' + str(max_val)
            res.append(cur)
        else:
            res.append(str(min_val))
        return res