class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        N   = len(s)
        
        vow_count1 , vow_count2 = 0 , 0
        
        for i in range(N//2):
            if s[i] in vow:
                vow_count1 += 1
                
                
        for j in range(N//2,N):
            if s[j] in vow:
                vow_count2 += 1  
                
        print("vow_count2",vow_count1,vow_count2)
        
        return vow_count1 == vow_count2
    
    
        #  ADD AND SUBTRACT 
        c, v, n = 0, set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']), len(s) // 2
        for i in range(n):
            if s[i] in v:
                c += 1
            if s[i+n] in v:
                c -= 1
        return c == 0