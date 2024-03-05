class Solution:
    def minimumLength(self, s: str) -> int:
        N = len(s)
        left , right = 0 , N -1
        
        while left < right:
            temp_left = left
            while left < right and  s[left] == s[right]:
                left += 1
            while temp_left < right and s[right] == s[temp_left]:
                right -= 1
            
            if s[left] != s[right]:
                break
            
        
        return max(0,right - left + 1)