class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap1 = {}
        for i in range(len(s)):
            if s[i] not in hashmap1:
                hashmap1[s[i]] = 1
            else:
                hashmap1[s[i]] += 1

        hashmap2 = {}
        for i in range(len(t)):
            if t[i] not in hashmap2:
                hashmap2[t[i]] = 1
            else:
                hashmap2[t[i]] += 1

        if len(hashmap1) != len(hashmap2):
            return False
        
        for k in hashmap1:
            if hashmap1.get(k) == hashmap2.get(k):
                pass
            else:
                return False
        return True