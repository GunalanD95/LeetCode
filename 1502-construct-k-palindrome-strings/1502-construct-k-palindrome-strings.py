from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        N = len(s)
        
        # If k is greater than the length of the string, it's impossible
        if k > N:
            return False
        
        # Count the frequency of each character
        freq = Counter(s)
        
        # Count how many characters have odd frequencies
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        
        # We can form k palindromic substrings if odd_count <= k
        return odd_count <= k

# Test case
sol = Solution()
print(sol.canConstruct("eminem", 2))  # Expected: True
print(sol.canConstruct("abc", 2))     # Expected: False
print(sol.canConstruct("aabbc", 3))   # Expected: True
