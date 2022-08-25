class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freqmag = {}

        for i in range(len(ransomNote)):
            if ransomNote[i] not in freqmag:
                freqmag[ransomNote[i]] = 1
            else:
                freqmag[ransomNote[i]] += 1


        for j in range(len(magazine)):
            if magazine[j] in freqmag:
                if freqmag[magazine[j]] == 1:
                    del freqmag[magazine[j]]
                else:
                    freqmag[magazine[j]] -= 1


        if len(freqmag) > 0:
            return False
        return True