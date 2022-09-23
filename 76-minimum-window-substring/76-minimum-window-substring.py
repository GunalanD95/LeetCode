from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        A , B = s , t 
        MapB  = Counter(B)
        n , k = len(A) , len(B)
        
        
        l , r = 0 , 0
        count = k
        min_len = n
        start , end = 0 , n-1

        found = False
        while r < n:
            if A[r] in MapB:
                MapB[A[r]] -= 1
                if MapB[A[r]] >= 0:
                    count -= 1
            r += 1


            if count > 0:
                continue

            while count == 0:
                if A[l] in MapB:
                    MapB[A[l]] += 1
                    if MapB[A[l]] > 0:
                        count += 1
                l += 1



            if (r - l) < min_len:
                found = True
                start = l
                end = r
                min_len = r - l
    
    
        if found:
            if start == 1:
                A[start:end]
            return A[start-1:end]
        
        return ""
    

        

        
                