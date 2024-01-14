from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        N, M = len(word1), len(word2)

        if N != M:
            return False

        if set(word1) != set(word2):
            return False

        counter1 = Counter(word1)
        counter2 = Counter(word2)

        return sorted(counter1.values()) == sorted(counter2.values())
