class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l , m = len(word1) , len(word2)
        out   = [''] * (l+m)
        
        i , j , k = 0 , 0 , 0 
        count = 1
        while i < l and j < m:
            if count & 1:
                out[k] = word1[i]
                i += 1
            else:
                out[k] = word2[j]
                j += 1
            count += 1
            k +=1

        while i < l:
            out[k] = word1[i]
            i += 1
            k += 1
            
        while j < m:
            out[k] = word2[j]
            j += 1
            k += 1
            
        return "".join(out)