class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N , M = len(text1) , len(text2)
        
        @cache
        def find_longest(i,j):
            if i == N or j == M:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + find_longest(i+1,j+1)
            else:
                return max(find_longest(i+1,j),find_longest(i,j+1))
            
        return find_longest(0,0)
        