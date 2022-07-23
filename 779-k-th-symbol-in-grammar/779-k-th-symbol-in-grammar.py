class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1 and k == 1: return 0   # base case
        
        total = ( 1 << n-1 )
        
        bound = total // 2
        
        if k > bound :   # right side
            b1 = k - bound
            return 1 - self.kthGrammar(n-1,b1)
            
        else:            # left side of the tree
        
            return self.kthGrammar(n-1,k)