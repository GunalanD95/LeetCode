class Solution:
    
    def reverse(self,string):
        return string[::-1]
    
    def invert(self,string):
        return ''.join('1' if ch == '0' else '0' for ch in string)
    
    def findKthBit(self, n: int, k: int) -> str:
        s1 = '0'
        for indx in range(2,n+1):
            s2 = s1 + '1' + self.reverse(self.invert(s1))
            s1 = s2  
        return s1[k-1]