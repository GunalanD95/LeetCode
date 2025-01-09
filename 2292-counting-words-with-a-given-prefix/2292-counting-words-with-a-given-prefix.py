class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        count = 0
        for wor in words:
            if wor.startswith(pref):
                count += 1

        return count
        