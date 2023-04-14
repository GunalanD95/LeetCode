class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Get the length of the input string
        N = len(s)  
        
        # Create a 2D list to store the lengths of palindromic substrings
        dp = [[-1] * (N+1) for _ in range(N+1)]
        
        # Define a recursive function to compute the length of the longest palindromic substring
        def DP(indx1,indx2):
            # If we have reached the end of the string, or the indices have crossed, return 0
            if indx1 >= N or indx2 < 0:
                return 0
            
            # If we have already computed the length of the longest palindromic substring for this range of indices,
            # return the stored value to avoid recomputing it
            if dp[indx1][indx2] != -1:
                return dp[indx1][indx2]
            
            # If the characters at the current indices match, recursively compute the length of the longest
            # palindromic substring for the substring between the current indices (i.e., exclude the matching
            # characters at the ends), and add 2 to account for the matching characters
            if s[indx1] == s[indx2]:
                dp[indx1][indx2] = DP(indx1+1,indx2-1) + 1
                
            # If the characters at the current indices do not match, compute the length of the longest palindromic
            # substring for both possible substrings obtained by excluding either the character at the first index or
            # the character at the second index, and take the maximum of the two lengths
            else:
                dp[indx1][indx2] = max (
                                       DP(indx1+1,indx2) ,
                                       DP(indx1,indx2-1) 
                )
            
            # Store the computed length of the longest palindromic substring in the 2D list to avoid recomputing it
            # in future recursive calls
            return dp[indx1][indx2]

        # Call the recursive function with the starting and ending indices of the entire string, and return the
        # computed length of the longest palindromic substring
        return DP(0,N-1)
