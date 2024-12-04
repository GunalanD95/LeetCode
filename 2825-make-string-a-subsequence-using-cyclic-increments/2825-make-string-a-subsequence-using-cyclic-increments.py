class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        N , M =  len(str1) , len(str2)
        i , j = 0 , 0
        
        count = 0
        while i < N and j < M:
            char = str2[j]
            if char == 'a':
                char2 = 'z'
            else:
                char2 = chr(ord(char)-1)
                
            char3 = str1[i]
            
            if char3 == char or char3 == char2:
                count += 1
                j += 1
            i += 1
        return count == M
            