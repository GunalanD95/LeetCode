class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n , k    = len(s) , len(t)
        min_len  = n
        flag     = False
        
        MapT     = Counter(t)
        count    = k
        
        
        st , end = 0 , n-1
        
        left,right = 0, 0
        
        
        while right < n:
            
            if s[right] in MapT:
                MapT[s[right]] -= 1

                if MapT[s[right]] >= 0:
                    count -= 1
            right += 1                

            if count > 0:
                continue 
            
            
            while count == 0:
                if s[left] in MapT:
                    MapT[s[left]] += 1
                    
                    if MapT[s[left]] > 0:
                        count += 1
                left += 1
            
            
            if (right - left) < min_len:
                min_len = right - left
                st      = left
                end     = right
                flag    = True
                
                
                
        
        if flag:
            if st == 1:
                s[st:end]
            return s[st-1:end]
        
        return ''
                
        