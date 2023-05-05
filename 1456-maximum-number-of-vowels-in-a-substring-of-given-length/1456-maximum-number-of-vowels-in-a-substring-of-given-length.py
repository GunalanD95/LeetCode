class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        N = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = sum(s[i] in vowels for i in range(k))
        res = count
        left = 0
        for right in range(k, N):
            if s[left] in vowels:
                count -= 1
            if s[right] in vowels:
                count += 1
            res = max(res, count)
            left += 1
        return res
