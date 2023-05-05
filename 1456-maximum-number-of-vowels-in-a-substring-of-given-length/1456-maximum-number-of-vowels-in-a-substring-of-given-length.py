class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        N = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # count vowels in the first window
        count = sum(s[i] in vowels for i in range(k))
        max_count = count

        # move the window by one character at a time
        for i in range(k, N):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            max_count = max(max_count, count)

        return max_count
