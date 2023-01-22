class Solution:
    def partition(self, s: str) -> List[List[str]]:
        string = list(s)
        N      = len(s)

        res = []
        
        def checkpalindrome(s):
            return s == s[::-1]
        
        def backtracking(indx,temp_str):
            if indx >= N or len(temp_str) >= N:
                temp = temp_str.copy()
                res.append(temp)
                return
            
            for j in range(indx,N):
                if checkpalindrome(s[indx:j+1]):
                    backtracking(j+1,temp_str + [s[indx:j+1]])
                
                
        
        backtracking(0,[])
        return res        